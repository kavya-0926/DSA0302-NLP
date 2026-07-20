import random

words = ["dog", "runs", "quickly"]

tags = {
    "dog": ["Noun"],
    "runs": ["Verb"],
    "quickly": ["Adverb"]
}

print("POS Tags:")

for word in words:
    print(word, "->", random.choice(tags[word]))