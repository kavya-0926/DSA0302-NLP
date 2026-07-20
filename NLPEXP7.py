import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = "Kavya is learning Python."

words = word_tokenize(text)

tags = pos_tag(words)

print(tags)