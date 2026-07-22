from nltk.wsd import lesk

sentence = "I went to the bank to deposit money"
word = "bank"

sense = lesk(sentence.split(), word)

print("Word:", word)

if sense:
    print("Sense:", sense.name())
    print("Meaning:", sense.definition())
else:
    print("No sense found")