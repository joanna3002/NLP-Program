import tkinter as tk
from tkinter import scrolledtext
import nltk
import spacy
from textblob import TextBlob
from nltk.corpus import stopwords

# Make sure required NLTK data is downloaded
nltk.download("stopwords")

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Stopwords
stop_words = set(stopwords.words("english"))

def analyze_text():
    text = input_box.get("1.0", tk.END).strip()

    if not text:
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, "Please enter text to analyze.")
        return

    doc = nlp(text)

    # Tokenization
    tokens = ", ".join([token.text for token in doc])

    # POS tagging
    pos_tags = "\n".join([f"{token.text} -> {token.pos_}" for token in doc])

    # Named Entities
    entities = "\n".join([f"{ent.text} ({ent.label_})" for ent in doc.ents]) or "None"

    # Lemmatization
    lemmatized = "\n".join([f"{token.text} -> {token.lemma_}" for token in doc])

    # Stopwords removal
    filtered_words = [word.text for word in doc if word.text.lower() not in stop_words]
    
    # Sentiment
    blob = TextBlob(text)
    sentiment = f"Polarity: {blob.sentiment.polarity}\nSubjectivity: {blob.sentiment.subjectivity}"

    # Keywords (simple method)
    keywords = ", ".join(set(filtered_words[:5]))

    # Display results
    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, "--- NLP ANALYSIS RESULTS ---\n\n")
    result_box.insert(tk.END, f"1. Tokens:\n{tokens}\n\n")
    result_box.insert(tk.END, "2. POS Tagging:\n" + pos_tags + "\n\n")
    result_box.insert(tk.END, "3. Named Entities:\n" + entities + "\n\n")
    result_box.insert(tk.END, "4. Lemmatized Words:\n" + lemmatized + "\n\n")
    result_box.insert(tk.END, f"5. Words after removing stopwords:\n{filtered_words}\n\n")
    result_box.insert(tk.END, "6. Sentiment Analysis:\n" + sentiment + "\n\n")
    result_box.insert(tk.END, f"7. Keywords:\n{keywords}\n\n")
    result_box.insert(tk.END, "--- END OF ANALYSIS ---")

# GUI window
window = tk.Tk()
window.title("NLP Text Analyzer")
window.geometry("700x600")

# Input label
tk.Label(window, text="Enter text to analyze:", font=("Arial", 12)).pack()

# Text input box
input_box = scrolledtext.ScrolledText(window, height=5, width=80)
input_box.pack()

# Analyze button
tk.Button(window, text="Analyze", font=("Arial", 12), command=analyze_text).pack(pady=10)

# Output results box
result_box = scrolledtext.ScrolledText(window, height=20, width=80)
result_box.pack()

# Start GUI loop
window.mainloop()
