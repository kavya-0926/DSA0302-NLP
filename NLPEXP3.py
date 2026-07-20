import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = "The students are studying Python."

words = word_tokenize(text)
tags = pos_tag(words)

print(tags)