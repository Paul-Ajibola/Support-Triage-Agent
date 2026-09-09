# tools/ticket_lookup.py
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv(".env.local")

def ticket_lookup(query: str, limit: int = 3) -> list[dict]:
    """Search historical tickets for similar past issues."""
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    cur = conn.cursor()
    cur.execute("""
        SELECT ticket_id, title, resolution, category
        FROM tickets
        WHERE title ILIKE %s OR body ILIKE %s
        LIMIT %s;
    """, (f"%{query}%", f"%{query}%", limit))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [
        {"ticket_id": r[0], "title": r[1], "resolution": r[2], "category": r[3]}
        for r in rows
    ]