import nltk

sentence = "The intelligent student reads a Python book"

words = sentence.split()

tagged = nltk.pos_tag(words)

grammar = "NP: {<DT>?<JJ>*<NN.*>+}"

parser = nltk.RegexpParser(grammar)

tree = parser.parse(tagged)

print("Noun Phrases:")

for subtree in tree.subtrees():
    if subtree.label() == "NP":
        words = [word for word, tag in subtree.leaves()]
        print(" ".join(words))