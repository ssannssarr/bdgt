""""Import Required Dependencies"""
from .storage import (
    load_data,
    save_data
)
import asyncclick as click
from rich.console import Console

console = Console()


@click.group()
def cli():
    pass


@cli.command()
@click.argument(
    'budget',
    required=True,
)
def set(
        budget: int | None
):
    data = load_data()
    data['budget'] = budget
    save_data(data)
    console.print(load_data())


if __name__ == "__main__":
    cli()
