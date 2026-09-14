from dataclasses import dataclass
from typing import Any


@dataclass
class TransactionSyncJob:
    """Job payload for processing external transaction synchronization."""

    source: str
    transactions: list[dict[str, Any]]

    def to_dict(self) -> dict[str, Any]:
        return {
            "source": self.source,
            "transactions": self.transactions,
        }


@dataclass
class CategorizationJob:
    """Job payload for transaction categorization."""

    transaction: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return {
            "transaction": self.transaction,
        }