"""
Writes security events (guardrail catches, tool validation failures)
to a persistent Postgres table, so attempted manipulation leaves a 
real, reviewable trail rather than only appearning in a single request's transient
state.
"""

import psycopg2
import os
from dotenv import load_dotenv


load_dotenv(".env.local")


def log_security_event(ticket_id: str, event_type: str, detail: str, ticket_body: str = "") -> None:
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    cur = conn.cursor()
    snippet = ticket_body[:200] if ticket_body else None
    cur.execute("""
        INSERT INTO security_audit_log (ticket_id, event_type, detail, ticket_body_snippet)
        VALUES (%s, %s, %s, %s);
    """, (ticket_id, event_type, detail, snippet))
    conn.commit()
    cur.close()
    conn.close()

