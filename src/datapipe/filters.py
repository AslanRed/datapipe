"""Filter functions that can be aplyed to csv files"""

from collections.abc import Generator
from reader import read_csv

def filter_by_emptys(func: Generator[list[str], None, None] = read_csv()) -> Generator[list[str], None, None]:
    for row in func:
        if "" in row:
            continue
        else:
            yield row
