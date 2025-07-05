import nltk
import os

NLTK_DIR = os.path.join(os.path.dirname(__file__), "../nltk_data")
os.makedirs(NLTK_DIR, exist_ok=True)

nltk.download("stopwords", download_dir=NLTK_DIR)
nltk.download("wordnet", download_dir=NLTK_DIR)
