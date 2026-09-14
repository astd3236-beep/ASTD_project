from datetime import date, datetime
from decimal import Decimal, InvalidOperation


def normalize_date(value: str) -> date:
    """Convert common date formats into a Python date."""
    value = value.strip()

    formats = [
        "%Y-%m-%d",
        "%d-%m-%Y",
        "%d/%m/%Y",
        "%m/%d/%Y",
        "%Y/%m/%d",
    ]

    for fmt in formats:
        try:
            return datetime.strptime(value, fmt).date()
        except ValueError:
            continue

    raise ValueError(f"Unsupported date format: {value}")


def normalize_amount(value: str) -> Decimal:
    """Convert a CSV amount into a Decimal."""
    value = value.strip().replace(",", "")

    try:
        return Decimal(value)
    except InvalidOperation:
        raise ValueError(f"Invalid amount: {value}")


def normalize_merchant(value: str) -> str:
    """Clean and standardize a merchant name."""
    return " ".join(value.strip().split())


def normalize_description(value: str) -> str:
    """Clean and standardize a transaction description."""
    return " ".join(value.strip().split())


def normalize_currency(value: str) -> str:
    """Normalize a currency code."""
    return value.strip().upper()


def normalize_account(value: str) -> str:
    """Clean and standardize an account name."""
    return " ".join(value.strip().split())