import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import RSLPStemmer


nltk.download('punkt')
nltk.download('stopwords')
nltk.download('rslp')
nltk.download('punkt_tab')

# def process_text_nlp_english(full_text):
#     # 1. Convert to lowercase
#     text = full_text.lower()
    
#     # 2. Tokenization (Transform string into a list of words)
#     words = word_tokenize(text)
    
#     # 3. Remove Stop Words and Punctuation
#     stops = set(stopwords.words('english'))
#     clean_words = [word for word in words if word.isalnum() and word not in stops]
    
#     # 4. Stemming (Reduce to root form)
#     stemmer = RSLPStemmer()
#     stemmed_words = [stemmer.stem(word) for word in clean_words]
    
#     return {
#         "clean": clean_words,
#         "stems": stemmed_words   
#     }

def process_text_nlp(full_text):
    # 1. Convert to lowercase
    text = full_text.lower()
    
    # 2. Tokenization (Transform string into a list of words)
    words = word_tokenize(text)
    
    # 3. Remove Stop Words and Punctuation
    stops = set(stopwords.words('portuguese'))
    clean_words = [word for word in words if word.isalnum() and word not in stops]
    
    # 4. Stemming (Reduce to root form)
    stemmer = RSLPStemmer()
    stemmed_words = [stemmer.stem(word) for word in clean_words]
    
    return {
        "clean": clean_words,
        "stems": stemmed_words   
    }