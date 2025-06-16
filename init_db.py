import sqlite3
import os

os.makedirs("data", exist_ok=True)
DB_PATH = "data/jobtrackr.db"

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS companies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    website TEXT
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER NOT NULL,
    position TEXT NOT NULL,
    date_applied TEXT NOT NULL,
    status TEXT NOT NULL,
    FOREIGN KEY (company_id) REFERENCES companies (id)
)
""")

conn.commit()
conn.close()
print(f"Database initialized at {DB_PATH}")
