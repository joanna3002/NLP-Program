# NLP GUI Text Analyzer

A Python-based Natural Language Processing (NLP) application with a **Graphical User Interface (GUI)** built using Tkinter.  
Analyze text for **tokens, POS tagging, named entities, lemmatization, stopwords removal, sentiment analysis, and keywords**.

---

## **Features**

- Tokenization
- Part-of-Speech (POS) tagging
- Named Entity Recognition (NER)
- Lemmatization
- Stopwords removal
- Sentiment analysis (Polarity & Subjectivity)
- Keyword extraction
- Simple, scrollable GUI using Tkinter

---

## **Requirements**

- Python 3.11 or 3.12  
- Libraries:

```bash
pip install spacy nltk textblob
python -m spacy download en_core_web_sm

Usage

Clone the repository:

git clone https://github.com/YOUR_USERNAME/NLP-Program.git
cd NLP-Program


Create and activate a virtual environment (Windows example):

python -m venv venv
.\venv\Scripts\Activate.ps1


Install dependencies:

pip install --upgrade pip
pip install -r requirements.txt
python -m spacy download en_core_web_sm


Run the GUI:

python nlp_gui.py


Enter your text in the GUI textbox and click Analyze to see results.
