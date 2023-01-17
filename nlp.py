#NitharshanCV_20BCE1732
#NLP_DA1

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import brown
from nltk.tokenize import sent_tokenize
from collections import defaultdict
from urllib import request
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer


text = brown.words()
text1 = ' '.join([str(elem) for elem in text])


brown.words(categories='government')
print(text1)

#1-Explore Brown Corpus and find the size, tokens, categories
print("Explore Brown Corpus and find the size, tokens, categories")
print(brown.categories())
#2-Find the size of word tokens
print("Find the size of word tokens")
print(len(word_tokenize(text1)))
#3-Find the size of the category “government” 
print("Find the size of the category “government” ") 
print(len(brown.words(categories='government')))
#4-List the most frequent tokens 
temp = defaultdict(int)
for sub in text1:
    for word in sub.split():
        temp[word] +=1
res = max(temp, key=temp.get)
print(str(res))

count = FreqDist(text1)
count.most_common()

#5-Count the number of sentences 
print("Count the number of sentences") 
number_of_sentences = sent_tokenize(text1)
print(len(number_of_sentences))

#2.1
#Raw Corpus
#transforming raw text
#The Internet is without a doubt the most significant source of literature. Existing text databases, like the corpora we looked at in earlier chapters, are useful to look over. You need to learn how to access your own text sources, though; you presumably already have some in mind.

#To answer these Questions:
#->How can we create software that can access text from both local files and the internet, giving us access to an infinite variety of linguistic resources?
#->How can the same kind of analysis that we performed on text corpora in prior chapters be applied to texts that have been broken up into individual words and punctuation marks?
#->How can we create software that generates formatted output and stores it in a file?

#2.1.1   Accessing Text from the Web 
url = "http://www.gutenberg.org/files/2554/2554-0.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')
type(raw)   
len(raw)
raw[:75]

#2.1.2 Strings: Text Processing at the Lowest Level

#Accessing Individual Characters
print(text[31])

#Accessing Substrings
print(text[-12:-7])
print( text[12:70])
#More Queries
lorem = """The Fulton County Grand Jury said Friday an investigation of Atlanta's recent primary election produced `` no evidence '' that any irregula
rities took place ."""
 
# upper() function to convert
# string to upper case
print("\nConverted String:")
print(lorem.upper())
 
# lower() function to convert
# string to lower case
print("\nConverted String:")
print(lorem.lower())
 
# converts the first character to
# upper case and rest to lower case
print("\nConverted String:")
print(lorem.title())
 
# original string never changes
print("\nOriginal String")
print(lorem)

#2.1.3 Extracting encoded text from files
path = nltk.data.find('C:\Users\Nitharshan Vijay\Downloads\dummytext.txt')
f = open(path, encoding='latin2')
for line in f:
    line = line.strip()
    print(line.encode('unicode_escape'))

#2.2 POS Tagging
#The practise of POS Tagging (Parts of Speech Tagging) involves marking up the text for a specific section of a speech depending on its meaning and context. 
#It is in charge of reading text in a language and giving each word a particular token (Parts of Speech). Another name for it is grammatical tagging.
#COUNTING POS TAGS
lower_case = text1.lower()
tokens = nltk.word_tokenize(lower_case)
tags = nltk.pos_tag(tokens)
counts = Counter( tag for word,  tag in tags)
print("COUNTING POS TAGS: number of tags=")
print(counts)
#Tagging Sentences
print("Tagging Sentences: ")
sen = nltk.sent_tokenize(text1)
for sent in sen:
	 print(nltk.pos_tag(nltk.word_tokenize(sent)))
#3.1  Word segmentation
#The challenge of breaking down a string of written language into its individual words is known as word tokenization (also known as word segmentation). 
# Space is a decent approximation of a word divider in English and many other languages that use some variation of the Latin alphabet.
sentences = nltk.sent_tokenize(text1)

for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    print(words)
    print()

#3.2 Sentence Tokenization
#The issue of breaking down a string of written language into its individual phrases is known as sentence tokenization, often referred to as sentence segmentation. 
#This concept seems extremely straightforward.When we encounter a punctuation mark, we may break apart the phrases in English and certain other languages.

for sentence in sentences:
    print(sentence)
    print()

#3.3 Convert to Lowercase
text = [token.lower() for token in text]
print(text)

#3.4 Stop words removal

  
stop_words = set(stopwords.words('english'))
  
word_tokens = word_tokenize(text1)
# converts the words in word_tokens to lower case and then checks whether 
#they are present in stop_words or not
filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
#with no lower case conversion
filtered_sentence = []
  
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
  
print(word_tokens)
print(filtered_sentence)

# 3.5 Stemming
#Stemming is a term that often describes a rudimentary heuristic method that removes derivational 
#affixes from words in the hopes of attaining this aim most of the time.
ps = PorterStemmer()
words = ["consultant", "consulting", "consults", "consulting", "consultative"]
  
for w in words:
    print(w, " : ", ps.stem(w)) 
#3.6 Lemmatization
#Lemmatization often refers to carrying out tasks correctly using a vocabulary and morphological analysis 
#of words, generally with the goal of removing only inflectional ends and returning the lemma, or dictionary form, of a word
lemmatizer = WordNetLemmatizer()
  
print("rocks :", lemmatizer.lemmatize("trees"))
print("corpora :", lemmatizer.lemmatize("children"))
  
# a denotes adjective in "pos"
print("better :", lemmatizer.lemmatize("better", pos ="a"))

#3.7 Part of speech tagger
#A POS tagger's main objective is to assign linguistic information, primarily grammatical information, to sub-sentential units.
#These units are referred to as tokens, and they typically correspond to words and symbols (e.g. punctuation).

stop_words = set(stopwords.words('english'))
tokenized = sent_tokenize(text)
for i in tokenized:
     
    # Word tokenizers is used to find the words
    # and punctuation in a string
    wordsList = nltk.word_tokenize(i)
 
    # removing stop words from wordList
    wordsList = [w for w in wordsList if not w in stop_words]
 
    #  Using a Tagger. Which is part-of-speech
    # tagger or POS-tagger.
    tagged = nltk.pos_tag(wordsList)
 
    print(tagged)
