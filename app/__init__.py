from flask import Flask, render_template, request
import os
import random

from .config import TEMPLATES_DIR, STATIC_DIR, DISPLAY_NAME_MAP
from .decks import list_decks, load_flashcards


def create_app() -> Flask:
    app = Flask(
        __name__,
        template_folder=str(TEMPLATES_DIR),
        static_folder=str(STATIC_DIR),
        static_url_path="/static",
    )

    @app.route("/")
    def index():
        # Determine available decks and selected deck
        decks = list_decks()
        default_deck = (
            "ai_flashcards" if "ai_flashcards" in decks else (decks[0] if decks else None)
        )
        selected_deck = request.args.get("deck") or default_deck
        if decks and selected_deck not in decks:
            selected_deck = default_deck

        # Load and shuffle deck
        cards = load_flashcards(selected_deck) if selected_deck else []
        random.shuffle(cards)

        # Asset cache-busting versions (mtime)
        def _asset_version(rel_path: str):
            try:
                full = os.path.join(app.static_folder, rel_path)
                return int(os.path.getmtime(full))
            except Exception:
                return None

        asset_versions = {
            "css": _asset_version("css/styles.css"),
            "js": _asset_version("js/app.js"),
        }

        return render_template(
            "index.html",
            cards=cards,
            deck_size=len(cards),
            decks=decks,
            selected_deck=selected_deck,
            display_names=DISPLAY_NAME_MAP,
            asset_versions=asset_versions,
        )

    return app
