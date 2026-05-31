"""Filter functions that can be aplyed to csv files"""

from collections.abc import Generator

from .reader import read_csv


def filter_by_emptys(
    func: Generator[list[str], None, None] = read_csv(),
) -> Generator[list[str], None, None]:
    for row in func:
        if "" in row:
            continue
        else:
            yield row


def filter_by_brand(
    brand_name: str, func: Generator[list[str], None, None] = read_csv()
) -> Generator[list[str], None, None]:
    for row in func:
        if brand_name == row[1]:
            yield row
        else:
            continue


def filter_by_year(
    product_year: int, func: Generator[list[str], None, None] = read_csv()
) -> Generator[list[str], None, None]:
    for row in func:
        if product_year == row[2]:
            yield row
        else:
            continue
