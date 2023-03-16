# ALICE V2.0 (Stable)
# Character count: 2439

import json
import nltk

# Download the 'punkt' resource (suppress download messages)
nltk.download('punkt', quiet=True)

# Set the NLTK data path
nltk.data.path.append(r'C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.2800.0_x64__qbz5n2kfra8p0\nltk_data')

from nltk.tokenize import word_tokenize

# Function to load Q&A pairs from the JSON file
def load_qa_pairs(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        qa_pairs = json.load(file)
    return qa_pairs

# Function to find a response for a given question using the loaded Q&A pairs
def find_response(qa_pairs, question):
    question_tokens = word_tokenize(question.lower())
    for pair in qa_pairs:
        if set(word_tokenize(pair["question"].lower())) == set(question_tokens):
            return pair["answer"]
    return None

# Update the process_input function to use the Q&A pairs
def process_input(user_input, qa_pairs):
    # Find a response from the Q&A pairs
    response = find_response(qa_pairs, user_input)

    # If no response is found, use the original keyword-based approach
    if not response:
        tokens = word_tokenize(user_input.lower())

        greetings = ['hello', 'hi', 'hey', 'greetings']
        farewells = ['bye', 'goodbye', 'see you']

        if any(token in greetings for token in tokens):
            response = "Hello! How can I help
