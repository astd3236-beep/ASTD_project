from abc import ABC, abstractmethod


class AIService(ABC):
    """Base interface for AI-powered services."""

    @abstractmethod
    def predict(self, transaction: dict) -> dict:
        """Generate an AI prediction for a transaction."""
        pass