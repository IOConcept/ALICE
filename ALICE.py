import nltk

# Download the 'punkt' resource
nltk.download('punkt')

# Set the NLTK data path
nltk.data.path.append(r'C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.2800.0_x64__qbz5n2kfra8p0\nltk_data')

from nltk.tokenize import word_tokenize

# Define a function to process user input and generate a response
def process_input(user_input):
    # Tokenize the user input
    tokens = word_tokenize(user_input.lower())

    # Define keywords and corresponding responses
    greetings = ['hello', 'hi', 'hey', 'greetings']
    farewells = ['bye', 'goodbye', 'see you']

    # Check if any keyword is present in the tokenized input
    if any(token in greetings for token in tokens):
        return "Hello! How can I help you?"
    elif any(token in farewells for token in tokens):
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond. Please try a different query."

# Main function to run ALICE
def main():
    print("Welcome to ALICE! (type 'quit' to exit)")

    while True:
        user_input = input("User: ")

        if user_input.lower() == 'quit':
            break

        response = process_input(user_input)
        print("ALICE:", response)

if __name__ == "__main__":
    main()
