import csv
from pathlib import Path

import pytest  # type: ignore

from src.datapipe.reader import read_csv


@pytest.mark.parametrize(
    "encoding, content",
    [
        # Test 1: utf-8 encoding
        ("utf-8", [["name", "age"], ["Jhon", "25"], ["Piter", "30"]]),
        # Test 2: windows-1251 encoding
        ("cp1251", [["id", "city"], ["1", "Moscow"], ["2", "Kazan"]]),
        # Test 3: utf-8 encoding with empty rows
        ("utf-8", [["header"], [], ["data"]]),
    ],
)
def test_read_csv_encodings(tmp_path: Path, encoding: str, content: list) -> None:
    # create temp file  in isolated dir
    test_file = tmp_path / "test_data.csv"

    # write to the temp file our test data
    with open(test_file, mode="w", encoding=encoding, newline="") as f:
        writer = csv.writer(f)
        writer.writerows(content)

    # call reader generator and collect results to list
    result = list(read_csv(file_path=test_file, encoding=encoding))

    # Check for origin data to be the same as output data
    assert result == content
