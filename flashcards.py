from flask import Flask, render_template, request
import random
import csv
import os

# Create the Flask app
app = Flask(__name__)

"""
Flashcard storage
Now backed by a CSV file at data/ai_flashcards.csv with headers: question,answer
This module loads the CSV at startup into a list of (question, answer) tuples.
"""

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
CSV_PATH = os.path.join(DATA_DIR, "ai_flashcards.csv")


def load_flashcards(csv_path: str):
    """Load flashcards from a CSV file.

    Returns a list of (question, answer) tuples. Skips blank rows.
    """
    cards = []
    try:
        with open(csv_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                q = (row.get('question') or '').strip()
                a = (row.get('answer') or '').strip()
                if q and a:
                    cards.append((q, a))
    except FileNotFoundError:
        # Fallback to empty list if file missing
        cards = []
    return cards

# -----------------------------------------------------------------
# FLASHCARD PROGRAM
# -----------------------------------------------------------------

def list_decks(data_dir: str):
    """Return a sorted list of available deck names (without .csv extension)."""
    try:
        files = [f for f in os.listdir(data_dir) if f.lower().endswith('.csv')]
        decks = sorted(os.path.splitext(f)[0] for f in files)
        return decks
    except FileNotFoundError:
        return []

@app.route("/")
def index():
    decks = list_decks(DATA_DIR)
    default_deck = 'ai_flashcards' if 'ai_flashcards' in decks else (decks[0] if decks else None)
    selected_deck = request.args.get('deck') or default_deck
    if decks and selected_deck not in decks:
        selected_deck = default_deck

    # Resolve path and load
    if selected_deck:
        csv_path = os.path.join(DATA_DIR, f"{selected_deck}.csv")
    else:
        csv_path = CSV_PATH
    cards = load_flashcards(csv_path)
    random.shuffle(cards)
    return render_template(
        "index.html",
        cards=cards,
        deck_size=len(cards),
        decks=decks,
        selected_deck=selected_deck
    )


# This line is needed for Vercel to run the app
if __name__ == "__main__":
    app.run()
    
