from datetime import date
from decimal import Decimal

from AI.app.backend_client import BackendClient
from AI.app.integrations import Integration
from AI.app.pipeline import TransactionPipeline


class FakeIntegration(Integration):
    def fetch_transactions(self) -> list[dict]:
        return [
            {
                "date": date(2026, 9, 14),
                "amount": Decimal("500.00"),
                "merchant": "Test Store",
                "description": "Test purchase",
                "currency": "INR",
                "account": "HDFC Bank",
            }
        ]

    def normalize_transactions(
        self, transactions: list[dict]
    ) -> list[dict]:
        return transactions


class FakeBackendClient(BackendClient):
    def __init__(self):
        self.received = []

    def send_transactions(self, transactions):
        self.received = transactions


integration = FakeIntegration()
backend = FakeBackendClient()

pipeline = TransactionPipeline(integration, backend)
result = pipeline.run()

assert len(result) == 1
assert result[0].merchant == "Test Store"
assert backend.received == result

print("Pipeline test: OK")