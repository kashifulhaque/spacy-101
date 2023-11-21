import spacy
from spacy.tokens import Doc

nlp = spacy.blank("en")

# Desired text: "spaCy is cool!"
words = ["spaCy", "is", "cool", "!"]
spaces = [True, True, False, False]

# Create a doc from the words and spaces
doc = Doc(nlp.vocab, words = words, spaces = spaces)
print(doc.text)

words = ["Go", ",", "get", "started", "!"]
spaces = [False, True, True, False, False]

doc = Doc(nlp.vocab, words = words, spaces = spaces)
print(doc.text)

words = ["Oh", ",", "really", "?", "!"]
spaces = [False, True, False, False, False]

doc = Doc(nlp.vocab, words = words, spaces = spaces)
print(doc.text)