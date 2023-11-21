"""
  First, we need to download SpaCy's trained pipeline
  Run `python -m spacy download en_core_web_sm` before running this file
"""
import spacy
nlp = spacy.load("en_core_web_sm")

text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"

doc = nlp(text)

for token in doc:
  # Get the token text
  token_text = token.text

  # Get the part-of-speech tag
  token_pos = token.pos_

  # Get the dependency label
  token_dep = token.dep_

  print(f"{token_text:<12}{token_pos:<10}{token_dep:<10}")

print("\n\n")
# Iterate over the predicted entities
for ent in doc.ents:
  # Print the entity text and its label
  print(ent.text, ent.label_)