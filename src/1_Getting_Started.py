import spacy

# Create a blank English object
nlp = spacy.blank("en")

# Process a sentence
doc = nlp("This is an english sentence.")

# Print the document text
print(doc.text)