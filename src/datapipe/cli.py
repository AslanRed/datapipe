import sys
from pathlib import Path

import typer

from .exceptions import ProcessingError
from .filters import filter_by_emptys
from .logger import logger
from .reader import read_csv
from .writer import write_csv

app = typer.Typer(help="DataPipe - csv files process")


@app.command()
def process(
    input: Path = typer.Option(..., "--input", "-i", help="Original CSV file"),
    output: Path = typer.Option(
        None, "--output", "-o", help="Where to save the result"
    ),
) -> None:
    """Filters rows of original csv by chosen filter and outputs the result"""
    if not input.exists():
        typer.echo(f"File not found: {input}", err=True)
        sys.exit(1)

    try:
        rows = read_csv(input)
        rows = filter_by_emptys(rows)

        if output:
            count = write_csv(rows, output)
            typer.echo(f"Rows saved: {count} -> {output}")
        else:
            count = 0
            for row in rows:
                typer.echo(",".join(row))
                count += 1
            typer.echo(f"\nRows total: {count}", err=True)

    except ProcessingError as e:
        logger.error(f"Error of processing: {e}")
        typer.echo(f"Error: {e}", err=True)
        sys.exit(1)


def main() -> None:
    app()
