import pickle

resume_lemmatized = pickle.load(open('../assets/resume_lemmatized.p', 'rb'))
print('Lemmatized Resume')
print(resume_lemmatized)
