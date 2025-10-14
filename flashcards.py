from flask import Flask, render_template
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

cards_list = load_flashcards(CSV_PATH)

@app.route("/")
def index():
    cards = list(cards_list)
    random.shuffle(cards)
    return render_template(
        "index.html",
        cards=cards,
        deck_size=len(cards)  # 👈 add this line
    )


# This line is needed for Vercel to run the app
if __name__ == "__main__":
    app.run()
    
