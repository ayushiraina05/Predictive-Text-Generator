import random

text = """
I love programming
I love machine learning
Machine learning is fun
Programming is powerful
"""

text = text.lower()
words = text.split()

model = {}

for i in range(len(words)-1):
    word = words[i]
    next_word = words[i+1]
    
    if word not in model:
        model[word] = []
    
    model[word].append(next_word)

def predict(word):
    if word in model:
        return random.choice(model[word])
    else:
        return "No suggestion found"

while True:
    user_input = input("Type a word: ").lower()
    print("Suggestion:", predict(user_input))
