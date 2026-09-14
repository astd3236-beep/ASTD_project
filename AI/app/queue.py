from .queue_config import (
    CATEGORIZATION_QUEUE,
    TRANSACTION_SYNC_QUEUE,
    get_redis_config,
)


class QueueConfig:
    """Provides AI queue and Redis configuration."""

    def redis(self) -> dict[str, int | str]:
        """Return Redis connection settings."""
        return get_redis_config()

    def queues(self) -> list[str]:
        """Return configured AI job queues."""
        return [
            TRANSACTION_SYNC_QUEUE,
            CATEGORIZATION_QUEUE,
        ]