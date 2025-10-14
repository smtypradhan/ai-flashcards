Overview"

The program provides a study guide to help students review key terms in AI. The flashcard approach presents a shuffled deck allowing them to focus, study, and track progress. It also keeps score at the end and lets you study the deck as many times as you want.

Program Requirements: 

1. Create a Python program to build flashcards.
2. The flashcards need to be shown one by one to help with focused and memory retention.
3. Deploy the Flask application to Vercel.
   
Final Output: 

○ Building initial Python web app, flask backend, requirements.txt, and basic UI.
○ Improved UI/UX styling for clarity and responsiveness. The design went through 15
versions of iterations
○ Finalized deployment configuration for stable release on Vercel. The app was deployed a total of 43 times before it was successfully launched.
○ Bug fixes and small code improvements.

Conclusion: 
Using Generative AI, I was able to build a Python program, accelerate development, streamline debugging, and achieve a professional-quality deployment. Different LLMs and software tools have been used for various aspects of the program. Some of them include Gemini AI, ChatGPT, ClaudeAI, Co-pilot, and a front-end cloud platform, Vercel,
for deploying the app, as well as Visual Studio for the build. Gemini AI provided the foundation, ChatGPT guided deployment, Claude AI enhanced design, and GitHub Copilot fine-tuned code. This iterative and collaborative process resulted in a successfully deployed, functional, and user-friendly Python application.

View the Program here:
https://ai-flashcards-smritipradhan.vercel.app/

Data source

- Flashcards live in CSV files under the `data/` folder with headers `question,answer`.
- The default deck is `data/ai_flashcards.csv`. You can add more decks by dropping additional `.csv` files into `data/` (e.g., `data/ml_basics.csv`).
- Select a deck from the dropdown on the homepage, or via URL query: `/?deck=ml_basics`.
- To edit or add cards, modify the CSV—each row becomes one card. The app shuffles cards each session.
