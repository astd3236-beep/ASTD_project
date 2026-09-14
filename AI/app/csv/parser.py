import csv
from pathlib import Path


class CSVParser:
    """Reads financial transactions from a CSV file."""

    def parse(self, file_path: str) -> list[dict[str, str]]:
        path = Path(file_path)

        with path.open("r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)
            return list(reader)