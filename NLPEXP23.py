sentences = [
    "Python is a programming language",
    "Python is used in machine learning",
    "Machine learning is used in AI"
]

score = 0

for i in range(len(sentences) - 1):

    words1 = set(sentences[i].lower().split())
    words2 = set(sentences[i + 1].lower().split())

    common = words1.intersection(words2)

    if common:
        score += 1

coherence = score / (len(sentences) - 1)

print("Coherence Score:", coherence)

if coherence > 0.5:
    print("Text is Coherent")
else:
    print("Text is Less Coherent")