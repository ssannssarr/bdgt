""""Import Required Dependencies"""
from .storage import (
    load_data,
    save_data
)
import asyncio
import time
import asyncclick as click
from rich.console import Console

console = Console()


@click.group()
async def cli():
    pass


@cli.command()
@click.argument(
    'budget',
    required=True,
)
async def set(
        budget: int | None
):
    data = load_data()
    data['budget'] = budget
    save_data(data)
    console.print(f"Budget set to ₹{load_data()['budget']}")


@cli.command()
@click.argument('purpose')
@click.argument('amount')
@click.option('--spent', is_flag=True)
@click.option('--gained', is_flag=True)
async def add(
        purpose: str,
        amount: int,
        spent,
        gained
):
    if spent == gained:
        raise click.UsageError(
            'Choose Only one --spent or --gained'
        )

    data = load_data()

    transaction = {
        'date': time.strftime('%d/%m/%Y'),
        'time': time.strftime("%H:%M"),
        'purpose': purpose,
        'amount': amount,
        'type': 'gained' if gained else 'spent'
    }

    data['transactions'].append(transaction)

    save_data(data=data)
    console.print(
        f"Added ₹{amount} as {'gained' if gained else 'spent'}"
    )


@cli.command()
def balance():
    data = load_data()

    budget = int(
        data['budget']
    )

    spent = sum(
        int(
            trnsct['amount']
        ) for trnsct in data['transactions'] if trnsct['type'] == 'spent'
    )

    gained = sum(
        int(
            trnsct['amount']
        ) for trnsct in data['transactions'] if trnsct['type'] == 'gained'
    )

    current_blnc = budget + gained - spent
    console.print(
        f"""
        BALANCE SUMMARY AT {time.strftime('%d/%m/%Y')}:
        Budget: {budget}
        Spent: {spent} [red]--[/]
        Gained: {gained} [green]++[/]
        Current Balance: {current_blnc}
        """
    )


@cli.command()
def refresh():
    data = load_data()
    data['budget'] = 0
    data['transactions'] = []

    save_data(data=data)
    console.print('[green]Refreshed Done!![/]')


if __name__ == "__main__":
    asyncio.run(cli())
