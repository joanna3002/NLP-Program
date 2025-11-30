import spacy
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords

# Download required NLTK datasets if not yet installed
nltk.download('punkt')
nltk.download('stopwords')

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Ask user for input
text = input("Enter a sentence or paragraph: ")
print("\n--- NLP ANALYSIS RESULTS ---")

# spaCy processing
doc = nlp(text)

# 1. Tokenization
print("\n1. Tokens:")
for token in doc:
    print(token.text, end=", ")

# 2. Part-of-Speech Tagging
print("\n\n2. POS Tagging:")
for token in doc:
    print(f"{token.text} -> {token.pos_}")

# 3. Named Entity Recognition
print("\n3. Named Entities:")
if doc.ents:
    for ent in doc.ents:
        print(f"{ent.text} ({ent.label_})")
else:
    print("No named entities found.")

# 4. Lemmatization
print("\n4. Lemmatized Words:")
for token in doc:
    print(f"{token.text} -> {token.lemma_}")

# 5. Stopword Removal
stop_words = set(stopwords.words("english"))
filtered = [word.text for word in doc if word.text.lower() not in stop_words and word.is_alpha]

print("\n5. Words after removing stopwords:")
print(filtered)

# 6. Sentiment Analysis using TextBlob
blob = TextBlob(text)
print("\n6. Sentiment Analysis:")
print(f"Polarity: {blob.sentiment.polarity}")
print(f"Subjectivity: {blob.sentiment.subjectivity}")

# 7. Keyword Extraction (simple method: filter nouns)
keywords = [token.text for token in doc if token.pos_ in ("NOUN", "PROPN")]
print("\n7. Keywords:")
print(keywords)

print("\n--- END OF ANALYSIS ---")
