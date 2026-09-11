"""
chekcpointing.py

To configure langgrap checkpointer backend (redis) used to persist
conversation state across turns, keyed by thread_id.
"""

import os
from langgrpah.checkpoint.redis import RedisSaver


def get_checkpointer():
    reddis_url = os.getenv("REDIS_URL", "redis://localhost:6379")
    return RedisSaver.from_conn_string(redis_url)

    