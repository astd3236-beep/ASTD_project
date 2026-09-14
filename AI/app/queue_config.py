import os


REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
REDIS_DB = int(os.getenv("REDIS_DB", "0"))

TRANSACTION_SYNC_QUEUE = "transaction-sync"
CATEGORIZATION_QUEUE = "transaction-categorization"


def get_redis_config() -> dict[str, int | str]:
    """Return Redis connection settings."""
    return {
        "host": REDIS_HOST,
        "port": REDIS_PORT,
        "db": REDIS_DB,
    }


def get_queue_names() -> list[str]:
    """Return the queues used by AI services."""
    return [
        TRANSACTION_SYNC_QUEUE,
        CATEGORIZATION_QUEUE,
    ]