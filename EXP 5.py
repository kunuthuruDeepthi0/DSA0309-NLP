from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["playing", "played", "studies", "running", "happily"]

for word in words:
    print(word, "->", ps.stem(word))
