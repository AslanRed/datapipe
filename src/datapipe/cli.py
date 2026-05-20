import sys
import typer
from pathlib import Path

from datapipe.reader import read_csv
from datapipe.filters import filter_by_emptys
from datapipe.writer import write_csv
from datapipe.config import settings
from datapipe,logger import logger
from datapipe.exceptions import ProcessingError

app = typer.Typer(help="DataPipe - csv files process")


@app.command()
    def process(
        input: Path = typer.Option(..., "--input", "-i", help="Original CSV file"),
        output: Path = typer.Option(None, "--output", "-o", help="Where to save the result"),
    ) -> None:
    """Filters rows of original csv by chosen filter and outputs the result"""
    if not input.exists():
        typer.echo(f"File not found: {input}", err=True)
        sys.exit(1)

    try:
        rows = read_csv(input)
        rows = filter_by_emptys(rows)

        if output:
            count = save_csv(rows, output)
            typer.echo(f"Rows saved: {count} -> {output}")
        else:
            count =0
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

