import spacy

# Create an English and German nlp object
nlp = spacy.blank("en")
nlp_de = spacy.blank("de")

# Get the ID for the string 'Bowie'
bowie_id = nlp.vocab.strings["Bowie"]
print(bowie_id)

# Look up the ID for "Bowie" in the vocab
print(nlp_de.vocab.strings[bowie_id])   # Will throw an error because the string "Bowie" is not in the German vocab
# Hence, the hash cannot be resolved in the string store
# Simply put, Hashes cannot be reversed