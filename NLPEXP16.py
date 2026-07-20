import spacy

# Load English model
nlp = spacy.load("en_core_web_sm")

text = "Kavya studies at Saveetha University in Chennai."

doc = nlp(text)

print("Named Entities:")
for ent in doc.ents:
    print(ent.text, "-", ent.label_)