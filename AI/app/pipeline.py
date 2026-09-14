from AI.app.backend_client import BackendClient
from AI.app.integrations import Integration
from AI.app.models import Transaction


class TransactionPipeline:
    """Coordinates fetching, normalization, and Backend delivery."""

    def __init__(
        self,
        integration: Integration,
        backend_client: BackendClient,
    ):
        self.integration = integration
        self.backend_client = backend_client

    def run(self) -> list[Transaction]:
        raw_transactions = self.integration.fetch_transactions()

        normalized_transactions = (
            self.integration.normalize_transactions(raw_transactions)
        )

        transactions = [
            Transaction(**transaction)
            for transaction in normalized_transactions
        ]

        self.backend_client.send_transactions(transactions)

        return transactions