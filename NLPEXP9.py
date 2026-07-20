import re

words = ["running", "played", "cats", "beautiful", "quickly"]

for word in words:
    if re.search("ing$", word):
        tag = "Verb"
    elif re.search("ed$", word):
        tag = "Verb"
    elif re.search("ly$", word):
        tag = "Adverb"
    elif re.search("s$", word):
        tag = "Noun"
    else:
        tag = "Adjective"

    print(word, "->", tag)