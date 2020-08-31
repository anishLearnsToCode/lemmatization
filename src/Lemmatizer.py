from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import nltk
import pickle
from nltk.tokenize import word_tokenize

# nltk.download('wordnet')

# lemmatizer = WordNetLemmatizer()
# print(lemmatizer.lemmatize('rocks'))

# running = wordnet.synsets('running', pos=wordnet.VERB)
# print(type(running))ste
# print('running:', running)
#
# first: nltk.corpus.reader.wordnet.Synset = running[1]
# print(type(first))
# print(first.definition())


class Lemmatizer:
    def __init__(self):
        self._lemmatizer = WordNetLemmatizer()
        self._tokenizer = nltk.RegexpTokenizer(r'\w+')

    def _tokenize(self, document: str) -> list:
        return self._tokenizer.tokenize(document)

    def lemmatize_word(self, word: str, pos=None) -> str:
        return self._lemmatizer.lemmatize(word, pos) if pos is not None else self._lemmatizer.lemmatize(word)

    def lemmatize_sentence(self, sentence: str, pos=None) -> str:
        result = []
        for word in self._tokenize(sentence):
            if pos is not None:
                result.append(self.lemmatize_word(word, pos))
            else:
                result.append(self.lemmatize_word(word))
        return ' '.join(result)

    def lemmatize_document(self, document: str) -> str:
        result = []
        for line in document.split('\n'):
            result.append(self.lemmatize_sentence(line))
        return '\n'.join(result)
