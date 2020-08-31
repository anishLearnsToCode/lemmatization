from src.Lemmatizer import Lemmatizer
import pickle


lemmatizer = Lemmatizer()
resume_file = open('../assets/resume.txt')
resume = resume_file.read().lower()
resume_file.close()

resume_lemmatized = lemmatizer.lemmatize_document(resume)
pickle.dump(resume_lemmatized, open('../assets/resume_lemmatized.p', 'wb'))

resume_lemmatized_file = open('../assets/resume_lemmatized.txt', 'w')
resume_lemmatized_file.write(resume_lemmatized)
resume_lemmatized_file.close()
