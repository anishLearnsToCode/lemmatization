# Lemmatization 

__Anish Sachdeva (DTU/2K16/MC/013)__

__Natural Language Processing - Dr. Seba Susan__

[📓 Jupyter Notebook](notebook/lemmatization.ipynb) |
[📄 Input](assets/resume.txt) |
[📄 Stemmed Output](assets/resume_stemmed.txt) |
[📄 Lemmatized Output](assets/resume_lemmatized.txt) | 
[📐 Project]()

![lemmatization](assets/lemmatization.png) 

## Overview
1. [Introduction](#introduction)
1. [Implementation](#implementation)
1. [Results](#results)
1. [Analytics & Discussion](#analytics--discussion)
1. [Running the Project Locally](#running-project-locally)
1. [Bibliography](#bibliography)

## Introduction
For grammatical reasons, documents are going to use different forms of a word, such as organize, organizes, and 
organizing. Additionally, there are families of derivationally related words with similar meanings, such as democracy, 
democratic, and democratization. In many situations, it seems as if it would be useful for a search for one of 
these words to return documents that contain another word in the set.

The goal of both stemming and lemmatization is to reduce inflectional forms and sometimes derivationally related 
forms of a word to a common base form. Stemming follows a heuristic approach to reducing the stem wherein the 
stemmer word will have similar character strings and may or may not be a valid dictionary word e.g.

```txt
happy --> happi
running --> run
```

The lemmatizer on the other hand doesn't follow a heuristic approach in reducing the word and will instead 
use a lookup table to refer to the various forms and meanings the word can possess and will also look up the 
surrounding context of the word to determine the correct POS (Part of Speech) Tag, which is then used to find the
__lexeme__ of the word. The lexeme is a valid english word and doesn't necessarily have to have a similar chracter
(root) structure e.g.

```txt
better --> good
wolves --> wolf
```  

We implement the lemmitizer using the Python __nltl__ package and apply it on a resume and compare the output with a
stemmed form of the same resume. Further Analytics and discussion give a deep dive into advantages, disadvantages and 
uses cases of lemmitization.

## Implementation
The following Helper classes have been used to create the stemmed output, lemmatize and 
Tokenize the output.

- [PorterStemmer](src/PorterStemmer.py)
- [Lemmatizer](src/Lemmatizer.py)
- [Tokenizer](src/Tokenizer.py)

> _Tokenizer_ uses the __nltk.RegexpTokenizer__

> _Lemmatizer_ uses the __nltk.WordNetLemmatizer__

> _PorterStemmer_ has been implemented by 
> [@anishLearnsToCode](https://github.com/anishLearnsToCode). 
> See project [here](https://github.com/anishLearnsToCode/porter-stemmer).
 
Initially the resume is loaded as a string from the `assets/resume.txt` file. 2 outputs are 
created from this resume. One stemmed, one lemmatized. Both these outputs are compared and 
basic analysis is run on them in the `src/analytics.py` file.

## Results
⭐ [Stemmed Resume](assets/resume_stemmed.txt)

⭐ [Lemmatized Resume](assets/resume_lemmatized.txt)

## Analytics & Discussion

## Running Project Locally
Clone the repository on your machine and enter the project directory
```bash
git clone https://github.com/anishLearnsToCode/lemmatization.git
cd lemmatization
cd src
```

Load in the Resume and create a stemmed and lemmatized output 
```bash
python stem_resume.py
python lemmatize_resume.py
```

See the outputs of the original, stemmed and lemmatized resumes: 
```bash
python output_resume.py
python output_setmmed.py
python output_lemmatized.py
```

Run the Analytics on the Stemmed and Lemmatized outputs
```bash
python analytics.py
```

## Bibliography
1. [Speech & Language Processing ~Jurafsky](https://web.stanford.edu/~jurafsky/slp3/)
1. [nltk](https://www.nltk.org/)
1. [pickle](https://docs.python.org/3/library/pickle.html)
1. [Porter Stemmer Algorithm](http://tartarus.org/martin/PorterStemmer)
1. [Porter Stemmer Implementation ~anishLearnsToCode](https://github.com/anishLearnsToCode/porter-stemmer)
1. [NLTK WordNetInterface](https://www.nltk.org/howto/wordnet.html)
1. [NLTK Stem Submodule](http://www.nltk.org/api/nltk.stem.html)
