from nltk import CFG
from nltk.parse import ChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> 'The' N
N -> 'cat'
VP -> V
V -> 'sleeps'
""")

parser = ChartParser(grammar)

sentence = "The cat sleeps".split()

for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()