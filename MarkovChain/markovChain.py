# Markov Chain Generator
# Source: https://github.com/healeycodes/markov-chain-generator/blob/main/generate.py

import os
import random
import re

from pdfminer.high_level import extract_text

# Get all PDF files in the directory
def get_PDF_text(dir):
    text = ""
    base_path = '/mnt/d/myPython/myAI/MarkovChain/src' # Use base_path if os.path.join() is not working
    files = [
        # os.path.join('myAI', 'MarkovChain', 'src', name) for name in os.listdir(os.path.join('myAI', 'MarkovChain', 'src'))
        os.path.join(base_path, name) for name in os.listdir(base_path) # Use base_path if os.path.join() is not working

        if name.lower().endswith('.pdf')
    ]
    # Extract the text from each PDF file
    for file in files:
        text += "\n"
        text += extract_text(file)
    return text

# Clean the extracted text.
# Remove common non-essential content using regular expressions.
def clean_text(text):
    text = re.sub(r'\bPage\+\b', '', text) # Remove "Page" headers
    text = re.sub(r'hunchen@Beez:.*?\$', '', text, flags=re.MULTILINE) # Remove the command-line headers
    text = re.sub(r'http[s]?://\S+', '', text) # Remove URLs
    text = re.sub(r'[\d\W]+', ' ', text) # Remove non-word characters and numbers, but keep spaces
    text= re.sub(r'\s+', ' ', text).strip() # Collapse multiple spaces into one

    return text 


# Build Model
def build_model(source, state_size):
    source = source.split()
    model = {}
    for i in range(state_size, len(source)):
        current_word = source[i]
        previous_words = ' '.join(source[i-state_size:i])
        if previous_words in model:
            model[previous_words].append(current_word)
        else:
            model[previous_words] = [current_word]

    return model


# Generate Text
def generate_text(model, state_size, min_length):
    # Filters keys once, then choose from the filtered list
    def get_new_starter():
        uppercase_starters = [s.split(' ') for s in model.keys() if s[0].isupper()]
        if not uppercase_starters:
            raise ValueError("No valid uppercase starters found in the model.")
        return random.choice(uppercase_starters)

    # Initialize 'text' with the starting words
    text = get_new_starter()
    i = state_size
    max_iterations = 10000 # This can be Adjusted
    iterations = 0

    # Generate text the Markov model
    while iterations < max_iterations:
        key = ' '.join(text[i-state_size:i])
        if key not in model:
            text += get_new_starter()
            i += state_size # Adjust by state_size to maintain sequence length 
            iterations += 1
            continue

        next_word = random.choice(model[key])
        text.append(next_word)
        i += 1
        iterations += 1

        if i > min_length and text[-1][-1] == '.':
            break

    if iterations >= max_iterations:
        print("Reached maximum iterations without completing text generation.")
    return ' '.join(text)

# Main
if __name__ == "__main__":
    state_size = 4
    min_length = 100
    raw_text = get_PDF_text('src') # Name changed because the PDF is the raw text version, before cleaning.
    cleaned_text = clean_text(raw_text) # Clean the extracted PDF text.
    model = build_model(cleaned_text, state_size)

    # Debugging
    print("Extracted text length:", len(raw_text))
    print("Cleaned text length:", len(cleaned_text))
    print("Number of keys in model:", len(model))

    text = generate_text(model, state_size, min_length)
    print(text) 
    