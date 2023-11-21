"""
  First, we need to download SpaCy's trained pipeline
  Run `python -m spacy download en_core_web_sm` before running this file
"""
import spacy
nlp = spacy.load("en_core_web_sm")

text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"

doc = nlp(text)

print(doc.text)