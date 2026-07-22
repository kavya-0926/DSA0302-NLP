translations = {
    "hello": "bonjour",
    "good morning": "bonjour",
    "thank you": "merci",
    "how are you": "comment allez-vous",
    "i am happy": "je suis heureux",
    "i love you": "je t'aime",
    "goodbye": "au revoir"
}

text = input("Enter English text: ").lower()

if text in translations:
    print("French Translation:", translations[text])
else:
    print("Translation not found")