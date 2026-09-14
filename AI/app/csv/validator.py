import csv
from pathlib import Path


REQUIRED_COLUMNS = {
    "date",
    "amount",
    "merchant",
    "description",
    "currency",
    "account",
}


class CSVValidator:
    """Validates uploaded transaction CSV files."""

    def validate(self, file_path: str) -> None:
        path = Path(file_path)

        if path.suffix.lower() != ".csv":
            raise ValueError("Uploaded file must be a CSV.")

        if not path.exists():
            raise ValueError("CSV file does not exist.")

        if path.stat().st_size == 0:
            raise ValueError("CSV file is empty.")

        with path.open("r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)
            columns = set(reader.fieldnames or [])

        missing_columns = REQUIRED_COLUMNS - columns

        if missing_columns:
            raise ValueError(
                f"Missing required columns: {', '.join(sorted(missing_columns))}"
            )