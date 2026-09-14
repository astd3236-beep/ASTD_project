from dataclasses import asdict
from typing import Any

from .models import Transaction

def transaction_to_dict(transaction: Transaction) -> dict[str, Any]:
    """Convert a Transaction into a JSON-compatible dictionary."""
    data = asdict(transaction)
    data["date"] = transaction.date.isoformat()
    data["amount"] = str(transaction.amount)
    return data
