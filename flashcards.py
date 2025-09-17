from flask import Flask, render_template
import random, time

# This creates the web app
app = Flask(__name__)

# -----------------------------------------------------------------
# FLASHCARD DECK
# -----------------------------------------------------------------
# ai_flashcards = {
    "What is Artificial Intelligence (AI)?": "The development of computer systems that can perform tasks typically requiring human intelligence, such as visual perception, speech recognition, decision-making, and translation.",
    "When and where was the term 'AI' coined?": "At Dartmouth College in 1956.",
    "Who is considered the 'father of AI' and what was his definition?": "John McCarthy. He defined AI as 'The science and engineering of making intelligent machines, especially intelligent computer programs'.",
    "What are the main goals of AI?": "To create systems that can learn, reason, perceive, plan, and solve problems.",
    "What is Machine Learning (ML)?": "A subset of artificial intelligence that enables systems to learn from data and improve their performance over time without being explicitly programmed.",
    "What is the difference between AI and ML?": "AI is the broad concept of enabling computers to mimic human behavior, while ML is a specific subset of AI that allows machines to learn from data.",
    "What does training a machine learning model require?": "Lots of data and lots of computing power.",
    "What is Supervised Learning?": "A type of machine learning where the model is trained on labeled data, meaning the input-output pairs are provided during training.",
    "What is Generative AI (Gen AI)?": "A subset of AI focused on creating new, original content (e.g., images, text, music) based on learned patterns from large volumes of data.",
    "What is the difference between Traditional AI and Generative AI?": "Traditional AI is often rule-based or used for prediction (like spam filtering), while Generative AI learns from data to create new, original content.",
    "What are Large Language Models (LLMs)?": "Powerful software systems designed to understand, generate, and manipulate human language, text, and other media using deep learning on a massive scale.",
    "What are Neural Networks?": "Algorithms modeled after the human brain, consisting of layers of interconnected nodes (neurons) that process data to identify patterns and make decisions.",
    "How do neural networks operate?": "The Input Layer receives data; weights are assigned to inputs; inputs are multiplied by weights and summed; an Activation Function determines if the node 'fires'; and data passes to the next layer.",
    "What are the three layers of a neural network?": "Input layer (receives data), Hidden layer(s) (processes data), and Output layer (produces the final result).",
    "What is Natural Language Processing (NLP)?": "A branch of AI focused on enabling computers to understand, interpret, and generate human language.",
    "What is Natural Language Understanding (NLU)?": "A branch of NLP that converts the natural language spoken by humans into structured data.",
    "What two tasks does NLU perform?": "Intent classification (understanding what a user is trying to accomplish) and entity extraction (recognizing key information like time, place, or name).",
    "What is Computer Vision?": "An AI field that enables machines to interpret and process visual data from the world, such as still images and videos, and extract information from them.",
    "Computer vision is based on the analysis of what values in an image?": "Pixels. A computer sees an image as an array holding number values for color and intensity.",
    "What is Optical Character Recognition (OCR)?": "A technique used in computer vision for extracting text from an image.",
    "What is Semantic Segmentation?": "An advanced machine learning technique in which individual pixels in an image are classified according to the object to which they belong.",
    "What is a chatbot?": "An AI-driven program designed to simulate conversation with human users, typically through text or voice.",
    "What is Conversational AI?": "A set of technologies (like chatbots and speech-based assistants) that enable computers to simulate conversations and automate communication.",
    "What is an 'agent' in AI?": "Anything that can perceive its environment through sensors and act upon that environment through effectors.",
    "What are the 5 components of 'intelligence' in AI?": "Reasoning, Learning, Problem Solving, Perception, and Linguistic Intelligence.",
    "What is an algorithm?": "A set of pre-defined rules and instructions, designed to solve a specific problem, in both a correct and efficient manner.",
    "What is data mining?": "The process of analyzing large datasets to find useful patterns, trends, or relationships that can be used for decision-making.",
    "What is Knowledge Mining?": "The process of extracting information from large volumes of often unstructured data to create a searchable knowledge store.",
    "What are AI ethics?": "Ensuring the fair, responsible, and transparent use of AI technologies, particularly around issues like bias, privacy, and accountability.",
    "What are some reasons AI-generated results might be inaccurate?": "Data Quality and Bias, Ambiguity in User Input, Limitations in Training, Overgeneralization, Misalignment with User Intent, and Limitations in Reasoning.",
    "What processor is ideal for large datasets and complex ML calculations?": "GPU (Graphics Processing Unit).",
    "Compare CPU, GPU, and TPU.": "CPU: General-purpose, few powerful cores for sequential tasks. GPU: High parallelism (ability to perform thousands of computations simultaneously), executed by thousands of cores for tasks like AI training. TPU: Specialized hardware by Google *specifically* for AI workloads (matrix operations).",
    "What are some applications of AI in healthcare?": "Disease diagnosis, personalized treatment plans, drug discovery, and robotic surgery.",
    "What are some applications of AI in finance?": "Algorithmic trading, fraud detection, risk management, credit scoring, and personalized financial services.",
    "What are the 4 general ways AI enables Self-Driving Cars?": "Sensing and Perception, Decision-Making and Control, Mapping and Localization, and Safety and Redundancy.",
    "What are the 5 main pillars of Azure Cognitive Services?": "Language, Speech, Web Search, Vision, and Decision.",
    "What is a major environmental impact of Generative AI?": "High electricity consumption for training and queries, expansion of energy-intensive data centers, and vast water usage for cooling."
}

# -----------------------------------------------------------------
# FLASHCARD PROGRAM
# -----------------------------------------------------------------

# Convert the dictionary to a list of (term, definition) items
cards_list = list(ai_flashcards.items())

# This is the main page of your website
@app.route('/')
def home():
    # Pick one random card from the list
    term, definition = random.choice(cards_list)
    
    # Send that card's data to the HTML file
    return render_template('index.html', term=term, definition=definition)

# This line is needed for Vercel to run the app
if __name__ == "__main__":
    app.run()
    
