prompt = input("Enter a prompt: ")

responses = {
    "artificial intelligence":
    "Artificial Intelligence enables machines to learn, reason, and solve problems like humans.",

    "machine learning":
    "Machine Learning allows computers to learn patterns from data and make predictions.",

    "nlp":
    "Natural Language Processing helps computers understand and process human language."
}

prompt_lower = prompt.lower()

found = False

for topic in responses:
    if topic in prompt_lower:
        print("\nGenerated Text:")
        print(responses[topic])
        found = True
        break

if not found:
    print("\nGenerated Text:")
    print("This is a generated response based on the given prompt.")