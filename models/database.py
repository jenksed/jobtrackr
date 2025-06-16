import sqlite3
import os

DB_PATH = os.path.join("data", "jobtrackr.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def fetch_all_applications():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT a.id, c.name AS company, a.position, a.applied_date, a.status, a.notes
        FROM applications a
        LEFT JOIN companies c ON a.company_id = c.id
        ORDER BY a.applied_date DESC
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows