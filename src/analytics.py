import pickle
from collections import Counter
from nltk.tokenize import word_tokenize

resume_stemmed = pickle.load(open('../assets/resume_stemmed.p', 'rb'))
resume_lemmatized = pickle.load(open('../assets/resume_lemmatized.p', 'rb'))

# extracting tokens from both the stemmed and lemmatized outputs
stemmed_resume_tokens = word_tokenize(resume_stemmed)
lemmatized_resume_tokens = word_tokenize(resume_lemmatized)

# comparing no. of words and word frequencies in both stemmed and lemmatized outputs
stemmed_resume_frequencies = Counter(stemmed_resume_tokens)
lemmatized_resume_frequencies = Counter(lemmatized_resume_tokens)
print('No. of unique tokens/words in the stemmed output:', len(stemmed_resume_frequencies))
print('No. of unique tokens/words in the lemmatized output:', len(lemmatized_resume_frequencies))

# seeing the top 20 most common words in the stemmed and lemmatized outputs
print('\nTop 30 most common words/tokens in the stemmed output:\n', stemmed_resume_frequencies.most_common(30))
print('Top 30 most common words/tokens in the lemmatized output:\n', lemmatized_resume_frequencies.most_common(30))
