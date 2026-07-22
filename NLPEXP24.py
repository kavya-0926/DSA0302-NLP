dialog = [
    "Hello!",
    "How are you?",
    "I am fine."
]

for text in dialog:

    if "hello" in text.lower():
        act = "Greeting"

    elif text.endswith("?"):
        act = "Question"

    else:
        act = "Statement"

    print(text, "->", act)