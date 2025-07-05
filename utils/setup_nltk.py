import nltk
import os

NLTK_DIR = os.path.join(os.path.dirname(__file__), "../nltk_data")
os.makedirs(NLTK_DIR, exist_ok=True)

nltk.download("stopwords")
nltk.download("wordnet")
