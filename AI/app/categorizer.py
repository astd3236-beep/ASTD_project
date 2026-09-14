from AI.app.ai_services import AIService
from AI.app.categories import TransactionCategory


class TransactionCategorizer(AIService):
    """Baseline rule-based transaction categorizer."""

    def predict(self, transaction: dict) -> dict:
        text = " ".join(
            [
                str(transaction.get("merchant", "")),
                str(transaction.get("description", "")),
            ]
        ).lower()

        rules = {
            TransactionCategory.SALES_INCOME: [
                "sale",
                "customer payment",
                "revenue",
            ],
            TransactionCategory.SOFTWARE_EXPENSE: [
                "software",
                "subscription",
                "aws",
                "google cloud",
                "github",
            ],
            TransactionCategory.MARKETING_EXPENSE: [
                "advertising",
                "ads",
                "marketing",
            ],
            TransactionCategory.TRAVEL_EXPENSE: [
                "uber",
                "flight",
                "hotel",
                "travel",
            ],
            TransactionCategory.MEALS_EXPENSE: [
                "restaurant",
                "food",
                "cafe",
                "swiggy",
                "zomato",
            ],
            TransactionCategory.BANK_FEES: [
                "bank fee",
                "transaction fee",
                "service charge",
            ],
        }

        for category, keywords in rules.items():
            if any(keyword in text for keyword in keywords):
                return {
                    "category": category.value,
                    "confidence": 0.80,
                }

        return {
            "category": TransactionCategory.UNKNOWN.value,
            "confidence": 0.20,
        }