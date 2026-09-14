from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass
class Transaction:
    date: date
    amount: Decimal
    merchant: str
    description: str
    currency: str
    account: str