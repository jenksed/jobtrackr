import streamlit as st
from models.database import get_connection

def applications_table():
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
