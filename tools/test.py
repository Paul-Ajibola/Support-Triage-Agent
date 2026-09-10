from tools.ticket_lookup import ticket_lookup

print(ticket_lookup("login"))

from tools.sandbox_runner import sandbox_runner
print(sandbox_runner("print('hello from sandbox')"))
print(sandbox_runner("import time; time.sleep(10)", timeout=3))

from tools.account_context_db import account_context_db
print(account_context_db("ACC-001"))

