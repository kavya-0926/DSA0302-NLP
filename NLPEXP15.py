from nltk import PCFG
from nltk.parse import ViterbiParser

grammar = PCFG.fromstring("""
S -> NP VP [1.0]
NP -> 'Kavya' [0.5] | 'Python' [0.5]
VP -> V NP [1.0]
V -> 'likes' [1.0]
""")

parser = ViterbiParser(grammar)

sentence = "Kavya likes Python".split()

for tree in parser.parse(sentence):
    print(tree)