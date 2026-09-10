# tools/test_tools.py
from tools.ticket_lookup import ticket_lookup
from tools.sandbox_runner import sandbox_runner
from tools.account_context_db import account_context_db

# Valid cases
assert ticket_lookup("login") != []
assert sandbox_runner("print(1+1)")["stdout"].strip() == "2"
assert account_context_db("ACC-001")["tier"] == "enterprise"

# Invalid/edge cases
assert ticket_lookup("zzznonexistent") == []
assert sandbox_runner("raise ValueError('boom')")["exit_code"] != 0
assert "error" in account_context_db("ACC-DOES-NOT-EXIST")

print("All tool tests passed.")

