import psycopg2, os

from dotenv import load_dotenv

load_dotenv(".env.local")

def account_context_db(account_id: str) -> dict:
    """Read-only lookup of account tier, spend, and rate limits."""
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    cur = conn.cursor()
    cur.execute("""
        SELECT account_id, tier, monthly_spend, rate_limit
        FROM accounts
        WHERE account_id = %s;
    """, (account_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if not row:
        return {"error": f"No account found for {account_id}"}
    return {"account_id": row[0], "tier": row[1], "monthly_spend": float(row[2]), "rate_limit": row[3]}

    