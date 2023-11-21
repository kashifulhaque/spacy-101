"""
  create the Doc and Span objects manually, and update the named entities - just like spaCy does behind the scenes.
"""
import spacy
from spacy.tokens import Doc, Span

nlp = spacy.blank("en")
words = ["I", "like", "David", "Bowie"]
spaces = [True, True, True, False]

# Create a Doc from the words and spaces
doc = Doc(nlp.vocab, words = words, spaces = spaces)
print(doc.text)

# Create a span for "David Bowie" from the doc and assign it to the label "PERSON"
span = Span(doc, start = 2, end = 4, label = "PERSON")
print(span.text, span.label_)

# Add the span to the doc's entities
doc.ents = [span]

# Print the entities' text and labels
print([(ent.text, ent.label_) for ent in doc.ents])