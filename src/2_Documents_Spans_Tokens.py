"""
  When you call nlp on a string, spaCy first tokenizes the text and creates a document object.
"""
import spacy

nlp = spacy.blank("en")

doc = nlp("Eating food is fun. However, I do not like sushi.")

# Print all the tokens
for token in doc:
  print(token.text, end = ' // ')
print()

# A slice of doc for "I do not like"
i_do_not_like = doc[7:11]
print(i_do_not_like.text)