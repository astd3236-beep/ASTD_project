from abc import ABC, abstractmethod


class Integration(ABC):
    """Base interface for external financial data integrations."""

    @abstractmethod
    def fetch_transactions(self) -> list[dict]:
        """Fetch raw transactions from an external source."""
        pass

    @abstractmethod
    def normalize_transactions(
        self, transactions: list[dict]
    ) -> list[dict]:
        """Convert raw transactions into our common format."""
        pass