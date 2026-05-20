import csv
from collections.abc import Generator
from pathlib import Path
from rich import print as rprint

from filters import filter_by_emptys
from decorators import check_for_ext


@check_for_ext
def write_csv(file_path: Path = Path("filtered.csv"), func: Generator[list[str], None, None] | None = None) -> None:
    with open(file_path, mode="w", encoding="utf-8") as out_f:
        writer = csv.writer(out_f, delimiter=",")

        if func is None:
            func = filter_by_emptys()

        count: int = 0
        for row in func:
            count += 1
            writer.writerow(row)
    rprint(f"[frame] Rows saved: {count}[/frame].")
    rprint("[bold]Completed![/bold]")
