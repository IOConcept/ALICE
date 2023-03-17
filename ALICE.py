# ALICE V2.4 (Approximate character count: 3800)
import json
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt', quiet=True)

def find_response(question, qa_pairs):
    tokens = set(word_tokenize(question.lower()))
    best_match = None
    max_common_tokens = 0
    threshold = 1

    for pair in qa_pairs:
        pair_tokens = set(word_tokenize(pair["question"].lower()))
        common_tokens = len(tokens.intersection(pair_tokens))

        if common_tokens > max_common_tokens:
            max_common_tokens = common_tokens
            best_match = pair["answer"]

    if max_common_tokens < threshold:
        return None

    return best_match

def load_qa_pairs(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_to_ac(file_path, question, explanation):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    data.append({"question": question, "answer": explanation})

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def process_input(user_input, sk_pairs, ac_pairs, ac_file_path):
    response = find_response(user_input, sk_pairs + ac_pairs)

    if not response:
        tokens = word_tokenize(user_input.lower())

        greetings = ['hello', 'hi', 'hey', 'greetings']
        farewells = ['bye', 'goodbye', 'see you']

        if any(token in greetings for token in tokens):
            response = "Hello! How can I help you?"
        elif any(token in farewells for token in tokens):
            response = "Goodbye! Have a great day!"
        else:
            response = None

    if not response:
        print("ALICE: I do not understand {}, please explain further.".format(user_input))
        user_explanation = input("User: ")
        save_to_ac(ac_file_path, user_input, user_explanation)
        response = "Thank you for explaining. I have added this information to my knowledge."

    return response

def main():
    sk_file_path = "SK.json"
    ac_file_path = "AC.json"
    sk_pairs = load_qa_pairs(sk_file_path)
    ac_pairs = load_qa_pairs(ac_file_path)

    print("Welcome to ALICE V2.4! (type 'quit' to exit)")

    while True:
        user_input = input("User: ")

        if user_input.lower() == 'quit':
            break

        response = process_input(user_input, sk_pairs, ac_pairs, ac_file_path)
        print("ALICE:", response)

if __name__ == "__main__":
    main()
