from src.PorterStemmer import PorterStemmer
import pickle

stemmer = PorterStemmer()
resume_file = open('../assets/resume.txt', 'r')
resume = resume_file.read().lower()
resume_file.close()

resume_stemmed = stemmer.stem_document(resume)
pickle.dump(obj=resume_stemmed, file=open('../assets/resume_stemmed.p', 'wb'))

resume_stemmed_file = open('../assets/resume_stemmed.txt', 'w')
resume_stemmed_file.write(resume_stemmed)
resume_stemmed_file.close()
