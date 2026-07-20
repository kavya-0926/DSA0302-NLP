import nltk
from nltk.util import bigrams

text = "I love natural language processing"

words = text.split()

bg = list(bigrams(words))

print("Bigrams:")
for b in bg:
    print(b)