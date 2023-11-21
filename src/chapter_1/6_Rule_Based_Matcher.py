"""
  spaCy’s rule-based Matcher
"""
import spacy
from spacy.matcher import Matcher
nlp = spacy.load("en_core_web_sm")

doc = nlp("Upcoming iPhone X release date leaked as Apple reveals pre-orders")

# Initialize the Matcher with shared vocabulary
matcher = Matcher(doc.vocab)

# Create a pattern matching two tokens: "iPhone" and "X"
pattern = [
  { "TEXT": "iPhone" },
  { "TEXT": "X" }
]

# Add the pattern to the matcher
matcher.add("IPHONE_X_PATTERN", [pattern])

# Use the matcher on "doc"
matches = matcher(doc)
print("Matches:", [doc[start:end].text for match_id, start, end in matches])