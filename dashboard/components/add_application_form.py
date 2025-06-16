import streamlit as st
from models.database import get_connection

def add_application_form(company_options):
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
            
            submitted = st.form_submit_button("Add Application")
            
            if submitted and selected_company:
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
