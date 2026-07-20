words = ["Ravi", "is", "running", "fast"]

tags = ["Noun", "Verb", "Noun", "Adjective"]

print("Before Transformation")

for i in range(len(words)):
    print(words[i], "->", tags[i])

# Transformation Rule:
# If a word ends with "ing", change its tag to Verb

for i in range(len(words)):
    if words[i].endswith("ing"):
        tags[i] = "Verb"

print("\nAfter Transformation")

for i in range(len(words)):
    print(words[i], "->", tags[i])