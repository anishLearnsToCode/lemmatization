import pickle
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
# nltk.download('wordnet')


def get_pos_frequency(tokens: list) -> Counter:
    synsets = [wordnet.synsets(token) for token in tokens]
    pos_tags = []
    for synset in synsets:
        if isinstance(synset, list) and len(synset) > 0:
            pos_tags.append(synset[0].pos())
    return Counter(pos_tags)


resume_file = open('../assets/resume.txt', 'r')
resume = resume_file.read().lower()
resume_file.close()
resume_stemmed = pickle.load(open('../assets/resume_stemmed.p', 'rb'))
resume_lemmatized = pickle.load(open('../assets/resume_lemmatized.p', 'rb'))

# extracting tokens from both the stemmed and lemmatized outputs
resume_tokens = word_tokenize(resume)
stemmed_resume_tokens = word_tokenize(resume_stemmed)
lemmatized_resume_tokens = word_tokenize(resume_lemmatized)

# Comparing the number of tokens in original, stemmed and lemmatized outputs
print('No. of tokens in Resume:', len(resume_tokens))
print('No. of tokens in Stemmed Resume:', len(stemmed_resume_tokens))
print('No. of tokens in Lemmatized Resume:', len(lemmatized_resume_tokens))

# comparing no. of words and word frequencies in both stemmed and lemmatized outputs
stemmed_resume_frequencies = Counter(stemmed_resume_tokens)
lemmatized_resume_frequencies = Counter(lemmatized_resume_tokens)
print('\nNo. of unique tokens/words in the stemmed output:', len(stemmed_resume_frequencies))
print('No. of unique tokens/words in the lemmatized output:', len(lemmatized_resume_frequencies))

# seeing the top 20 most common words in the stemmed and lemmatized outputs
print('\nTop 30 most common words/tokens in the stemmed output:\n', stemmed_resume_frequencies.most_common(30))
print('Top 30 most common words/tokens in the lemmatized output:\n', lemmatized_resume_frequencies.most_common(30))


# Analyzing of frequency of POS tags in original, stemmed and Lemmatized resume
resume_pos_frequency = get_pos_frequency(resume_tokens)
stemmed_resume_pos_frequency = get_pos_frequency(stemmed_resume_tokens)
lemmatized_resume_pos_frequency = get_pos_frequency(lemmatized_resume_tokens)

print('\nResume POS Tags Frequency:', resume_pos_frequency)
print('Stemmed Resume POS Tags Frequency:', stemmed_resume_pos_frequency)
print('Lemmatized Resume POS Tags Frequency:', lemmatized_resume_pos_frequency)
