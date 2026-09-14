from abc import ABC, abstractmethod

from AI.app.models import Transaction


class BackendClient(ABC):
    """Interface for sending normalized transactions to the Backend."""

    @abstractmethod
    def send_transactions(self, transactions: list[Transaction]) -> None:
        """Send normalized transactions to the Backend."""
        pass