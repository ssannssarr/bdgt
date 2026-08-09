"""Import Required Dependencies"""
from pathlib import Path
import json
from typing import Any

ROOT_DIR = Path.home()
DB_DIR = ROOT_DIR / '.budget'
DB_FILE = DB_DIR / 'budget.json'


DB_DIR.mkdir(
    parents=True,
    exist_ok=True
)


def load_data():
    if not DB_FILE.exists():
        return {
            'budget': 0,
            'transactions': []
        }
    return json.loads(
        DB_FILE.read_text(
            encoding='utf-8'
        )
    )


def save_data(
        data: dict[str, Any]
):
    DB_DIR.mkdir(
        parents=True,
        exist_ok=True
    )
    DB_FILE.write_text(
        json.dumps(
            data,
            indent=3
        )
    )
