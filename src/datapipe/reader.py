import csv
from collections.abc import Generator
from pathlib import Path

from decorators import check_for_ext

csv_path = Path("path.csv")

@check_for_ext
def read_csv(file_path: Path = csv_path) -> Generator[list[str], None, None]:
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                yield row
