from enum import StrEnum


class TransactionCategory(StrEnum):
    """Standard categories for transaction classification."""

    SALES_INCOME = "sales_income"
    OTHER_INCOME = "other_income"

    OFFICE_EXPENSE = "office_expense"
    TRAVEL_EXPENSE = "travel_expense"
    MEALS_EXPENSE = "meals_expense"
    SOFTWARE_EXPENSE = "software_expense"
    MARKETING_EXPENSE = "marketing_expense"
    RENT_EXPENSE = "rent_expense"
    UTILITIES_EXPENSE = "utilities_expense"
    PAYROLL_EXPENSE = "payroll_expense"
    PROFESSIONAL_SERVICES = "professional_services"
    BANK_FEES = "bank_fees"
    TAXES = "taxes"

    INVENTORY = "inventory"
    EQUIPMENT = "equipment"

    TRANSFER = "transfer"
    LOAN = "loan"

    REFUND = "refund"
    UNKNOWN = "unknown"