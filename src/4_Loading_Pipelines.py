"""
  First, we need to download SpaCy's trained pipeline
  Run `python -m spacy download en_core_web_sm` before running this file
"""
import spacy
nlp = spacy.load("en_core_web_sm")