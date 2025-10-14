import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"
DATA_DIR = BASE_DIR / "data"

# Friendly display names for known decks (keys are CSV basenames without extension)
DISPLAY_NAME_MAP = {
    "ai_flashcards": "Basics of AI",
    "ai_flashcards_set2": "ML, NN, Prompt Engineering",
}
