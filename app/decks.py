import csv
import os
from typing import List, Tuple

from .config import DATA_DIR


def list_decks() -> list[str]:
    """Return a sorted list of available deck names (without .csv extension)."""
    try:
        files = [f for f in os.listdir(DATA_DIR) if f.lower().endswith('.csv')]
        decks = sorted(os.path.splitext(f)[0] for f in files)
        return decks
    except FileNotFoundError:
        return []


def get_deck_path(deck_name: str) -> str:
    safe_name = os.path.basename(deck_name)
    filename = safe_name + '.csv' if not safe_name.lower().endswith('.csv') else safe_name
    return os.path.join(DATA_DIR, filename)


def load_flashcards(deck_name_or_path: str) -> List[Tuple[str, str]]:
    """Load flashcards from a deck name (basename) or absolute/relative CSV path.

    Returns a list of (question, answer) tuples. Skips blank rows.
    """
    # Resolve deck path if a name is provided
    path = deck_name_or_path
    if not os.path.sep in deck_name_or_path and not deck_name_or_path.lower().endswith('.csv'):
        path = get_deck_path(deck_name_or_path)

    cards: List[Tuple[str, str]] = []
    try:
        with open(path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                q = (row.get('question') or '').strip()
                a = (row.get('answer') or '').strip()
                if q and a:
                    cards.append((q, a))
    except FileNotFoundError:
        cards = []
    return cards
