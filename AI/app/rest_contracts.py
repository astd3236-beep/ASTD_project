from dataclasses import dataclass
from typing import Any

from .contracts import transaction_to_dict
from .models import Transaction


@dataclass
class TransactionSyncRequest:
    """REST request payload for sending transactions to the Backend."""

    transactions: list[Transaction]

    def to_dict(self) -> dict[str, Any]:
        return {
            "transactions": [
                transaction_to_dict(transaction)
                for transaction in self.transactions
            ]
        }


@dataclass
class TransactionSyncResponse:
    """REST response returned by the Backend after transaction sync."""

    success: bool
    received_count: int
    message: str

    @classmethod
    def from_dict(
        cls, data: dict[str, Any]
    ) -> "TransactionSyncResponse":
        return cls(
            success=bool(data.get("success", False)),
            received_count=int(data.get("received_count", 0)),
            message=str(data.get("message", "")),
        )