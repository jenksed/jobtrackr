import streamlit as st
from models.database import get_connection
from components.add_company_form import add_company_form
from components.add_application_form import add_application_form
from components.applications_table import applications_table

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load CSS
local_css("dashboard/static/style.css")


st.title("JobTrackr: Job Application Tracker")

# Add company form
add_company_form()

# Fetch companies for select box
conn = get_connection()
cursor = conn.cursor()
cursor.execute("SELECT id, name FROM companies ORDER BY name")
companies = cursor.fetchall()
conn.close()
company_options = {name: cid for cid, name in companies}

# Add application form
add_application_form(company_options)

# Applications table
applications_table()
