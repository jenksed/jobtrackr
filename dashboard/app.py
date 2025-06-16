import streamlit as st
from models.database import get_connection

st.title("JobTrackr: Job Application Tracker")

# Form: Add Company
with st.expander("➕ Add New Company"):
    with st.form("add_company_form"):
        company_name = st.text_input("Company Name")
        company_website = st.text_input("Company Website (optional)")
        submitted_company = st.form_submit_button("Add Company")
        
        if submitted_company:
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

# Fetch companies for select box
conn = get_connection()
cursor = conn.cursor()
cursor.execute("SELECT id, name FROM companies ORDER BY name")
companies = cursor.fetchall()
conn.close()

company_options = {name: cid for cid, name in companies}

# Form: Add Application
with st.expander("📄 Add New Application"):
    with st.form("add_application_form"):
        if company_options:
            selected_company = st.selectbox("Company", list(company_options.keys()))
        else:
            st.warning("⚠️ Add a company first!")
            selected_company = None

        position = st.text_input("Position Title")
        date_applied = st.date_input("Date Applied")
        status = st.selectbox("Status", ["Applied", "Interviewing", "Offer", "Rejected", "Other"])
        
        submitted_app = st.form_submit_button("Add Application")
        
        if submitted_app and selected_company:
            conn = get_connection()
            cursor = conn.cursor()
            try:
                cursor.execute(
                    """INSERT INTO applications (company_id, position, date_applied, status)
                       VALUES (?, ?, ?, ?)""",
                    (company_options[selected_company], position, date_applied.isoformat(), status)
                )
                conn.commit()
                st.success(f"Added application for {position} at {selected_company}")
            except Exception as e:
                st.error(f"Error: {e}")
            finally:
                conn.close()

# Display existing applications
st.subheader("📌 Tracked Applications")
conn = get_connection()
cursor = conn.cursor()
cursor.execute("""
    SELECT a.id, c.name, a.position, a.date_applied, a.status
    FROM applications a
    LEFT JOIN companies c ON a.company_id = c.id
    ORDER BY a.date_applied DESC
""")
rows = cursor.fetchall()
conn.close()

if rows:
    st.table([
        {
            "ID": r[0],
            "Company": r[1],
            "Position": r[2],
            "Date Applied": r[3],
            "Status": r[4]
        }
        for r in rows
    ])
else:
    st.info("No applications added yet.")
