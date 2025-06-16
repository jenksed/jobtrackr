import streamlit as st
from models.database import get_connection

def add_company_form():
    with st.expander("➕ Add New Company"):
        with st.form("add_company_form"):
            company_name = st.text_input("Company Name")
            company_website = st.text_input("Company Website (optional)")
            submitted = st.form_submit_button("Add Company")
            
            if submitted:
                conn = get_connection()
                cursor = conn.cursor()
                try:
                    cursor.execute(
                        "INSERT INTO companies (name, website) VALUES (?, ?)",
                        (company_name, company_website)
                    )
                    conn.commit()
                    st.success(f"Added company: {company_name}")
                except Exception as e:
                    st.error(f"Error: {e}")
                finally:
                    conn.close()
