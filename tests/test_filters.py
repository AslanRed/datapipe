import csv
from pathlib import Path

import pytest  # type: ignore

from src.datapipe import filters
from src.datapipe.reader import read_csv


@pytest.mark.parametrize(
    "encoding, content",
    [
        # Content to test filter_by_empty
        (
            "utf-8",
            [
                ["brand", "year"],
                ["BMW", "1995"],
                ["Jaguar", ""],
                [" ", "2003"],
                ["", ""],
            ],
        )
    ],
)
def test_filter_by_emptys(tmp_path: Path, encoding: str, content: list) -> None:
    # create tmp file in isolated dir
    test_file = tmp_path / "test_data.csv"

    # write the tmp file
    with open(test_file, mode="w", encoding=encoding, newline="") as f:
        writer = csv.writer(f)
        writer.writerows(content)

    # call filter_by_emptys
    result = list(
        filters.filter_by_emptys(read_csv(file_path=test_file, encoding=encoding))
    )

    expected = [["brand", "year"], ["BMW", "1995"], [" ", "2003"]]

    # check result
    assert result == expected
