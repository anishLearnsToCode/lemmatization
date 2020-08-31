import nltk


class Tokenizer:
    def __init__(self):
        self._tokenizer = nltk.RegexpTokenizer(r'\w+')

    def tokenize(self, document: str) -> list:
        return self._tokenizer.tokenize(document)
