import csv
from typing import Optional, Generator
from pathlib import Path

file_path = Path("path.csv")

def read_csv(file_path: Path = file_path) -> Optional[Generator[list[str], None, None]]:
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                yield row
    except Exception as e:
        print(e)
    return None
