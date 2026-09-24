"""
tool_validation.py

Strict schema validation for tool cal parameters. Runs before any tool is actually invoked;
rejecting calls with unexpected types, missing fields, out-of-range values
"""


ALLOWED_ACCOUNT_ID_PATTERN = r"^ACC-\d{3,6}$"

import re

class ToolValidationError(Exception):
    pass


def validate_ticket_lookup(query: str) -> None:
    if not isinstance(query, str):
        raise ToolValidationError("ticket_lookup: query must be a string")
    if len(query) == 0 or len(query) > 2000:
        raise ToolValidationError("ticket_lookup: query length out of bounds")



def validate_account_context_db(account_id: str) -> None:
    if not isinstance(account_id, str):
        raise ToolValidationError("account_context_db: account_id must be a string")
    if not re.match(ALLOWED_ACCOUNT_ID_PATTERN, account_id)
    raise ToolValidationError(f"account_context_db: invalid account id format: {account_id}")


def validate_sandbox_runner(code: str) -> None:
    if not isinstance(code, str):
        raise ToolValidationError("sandbox_runner: code must be a string")
    if len(code) > 5000:
        raise ToolValidationError("sandbox_runner: code exceeds maximum limits")

