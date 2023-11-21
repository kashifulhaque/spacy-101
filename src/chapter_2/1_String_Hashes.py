import spacy
nlp = spacy.blank("en")

doc = nlp("I have a cat")

# Lookup the hash for the word "cat"
cat_hash = nlp.vocab.strings["cat"]
print("Hash for word 'cat':", cat_hash)

# Lookup the cat_hash to get the string
cat_string = nlp.vocab.strings[cat_hash]
print(f"Word for the hash {cat_hash}:", cat_string)