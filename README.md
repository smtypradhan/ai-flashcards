Overview

The program provides a study guide to help students review key terms in AI. The flashcard approach presents a shuffled deck allowing them to focus, study, and track progress. It also keeps score at the end and lets you study the deck as many times as you want.

Objectives:

1) Create a Python program to build flashcards.
2) The flashcards need to be shown one by one to help with focused and memory retention.
3) Deploy the Flask application to Vercel.
   
1st Iteration - Output: 

○ Building initial Python web app, flask backend, requirements.txt, and basic UI.
○ Improved UI/UX styling for clarity and responsiveness. The design went through 15
versions of iterations
○ Finalized deployment configuration for stable release on Vercel. The app was deployed a total of 43 times before it was successfully launched.
○ Bug fixes and small code improvements.

Conclusion: 
Using Generative AI, I was able to build a Python program, accelerate development, streamline debugging, and achieve a professional-quality deployment. Different LLMs and software tools have been used for various aspects of the program. Some of them include Gemini AI, ChatGPT, ClaudeAI, Co-pilot, and a front-end cloud platform, Vercel,
for deploying the app, as well as Visual Studio for the build. Gemini AI provided the foundation, ChatGPT guided deployment, Claude AI enhanced design, and GitHub Copilot fine-tuned code. This iterative and collaborative process resulted in a successfully deployed, functional, and user-friendly Python application.

<!-- App screenshot -->
<p align="center">
	<img src="static/images/ai-flashcards-screenshot.png" alt="AI Flashcards screenshot" width="700">
</p>


View the Program here:
https://ai-flashcards-smritipradhan.vercel.app/

Data source

- Flashcards live in CSV files under the `data/` folder with headers `question,answer`.
- The default deck is `data/ai_flashcards.csv`. You can add more decks by dropping additional `.csv` files into `data/` (e.g., `data/ml_basics.csv`).
- Select a deck from the dropdown on the homepage, or via URL query: `/?deck=ml_basics`.
- To edit or add cards, modify the CSV—each row becomes one card. The app shuffles cards each session.

Project structure

```
flashcards.py                 # Thin entry used by Vercel to create the Flask app
app/
	__init__.py                 # create_app(), route definitions, asset versioning
	decks.py                    # CSV loading and deck discovery utilities
	config.py                   # Paths (templates/static/data) and deck display names
templates/
	index.html                  # App template
static/
	css/styles.css              # All styles
	js/app.js                   # All client-side behavior (flip, arrows, shuffle, score)
	sounds/card-flip.wav        # Flip sound effect
data/
	ai_flashcards.csv           # Basics of AI
	ai_flashcards_set2.csv      # ML, NN, Prompt Engineering
requirements.txt
vercel.json
```

Run locally

1) Install dependencies
2) Run the server

The app exposes Flask at `flashcards.py:app`.

Deployment (Vercel)

- `vercel.json` routes all requests to `flashcards.py` using the Python runtime.
- Static assets are cache-busted with a `?v=<mtime>` query string to avoid stale CSS/JS.

Usage and controls

- Choose a deck from the dropdown (friendly names shown).
- Click Start or press Enter to begin.
- Navigate: use the left/right arrow icons next to the card, or keyboard ← →.
- Flip card: button or Space/Enter.
- Mark on back of card: G (correct), M (missed).
- Shuffle: reshuffles the current deck mid-session.


