import json
import nltk

# Download the 'punkt' resource
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
    for pair in qa_pairs:
        if pair["question"].lower() == question.lower():
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
            response = "Hello! How can I help you?"
        elif any(token in farewells for token in tokens):
            response = "Goodbye! Have a great day!"
        else:
            response = "I'm not sure how to respond. Please try a different query."

    return response

# Update the main function to load Q&A pairs and pass them to the process_input function
def main():
    print("Welcome to ALICE V1.1! (type 'quit' to exit)")

    # Load Q&A pairs from the JSON file
    qa_pairs = load_qa_pairs('SK.json')

    while True:
        user_input = input("User: ")

        if user_input.lower() == 'quit':
            break

        response = process_input(user_input, qa_pairs)
        print("ALICE:", response)

if __name__ == "__main__":
    main()
