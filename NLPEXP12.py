from nltk import CFG
from nltk.parse import EarleyChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> 'Kavya'
VP -> V NP
V -> 'likes'
NP -> 'Python'
""")

parser = EarleyChartParser(grammar)

sentence = "Kavya likes Python".split()

for tree in parser.parse(sentence):
    print(tree)