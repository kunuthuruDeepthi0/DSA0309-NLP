import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')

words = ["playing", "played", "studies", "running"]

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

for word in words:
    print("Word:", word)
    print("Stem:", stemmer.stem(word))
    print("Lemma:", lemmatizer.lemmatize(word, pos='v'))
    print()
