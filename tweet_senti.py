import imp
import nltk
from nltk.corpus import names
from nltk import *

import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names
from nltk.corpus import stopwords
from nltk import NaiveBayesClassifier
from nltk import classify

import pandas as pd
from nltk.corpus import movie_reviews

import string

def sent_ext():
	fob = open ("alert.txt", "r+")
	article = fob.read()

	words = word_tokenize(article)
	sentence = sent_tokenize(article)

	list_of_english_stopwords =  (stopwords.words('english'))

	words = [w for w in words if w.isalpha()]
	words_filtered = words[:]

	for word in words:
		if (word in list_of_english_stopwords):
			words_filtered.remove (word)

	inp = int(input("To clean text, press  1- Stemming  (OR)  2- Lemmatization: "))
	if (inp == 1):
		words_stem = stem(words)

	elif (inp == 2):
		words_lemm = lemm(words)

	else:
		print ("Invalid input !")

#--

def stem(words):
	stemmer = PorterStemmer()

	words_stem = []
	for word in words:
		words_stem.append (stemmer.stem(word))

	print (words_stem)

#--


def lemm(words):
	lemmatizer = WordNetLemmatizer()

	words_lemm = []
	for word in words:
		words_lemm.append (lemmatizer.lemmatize(word))

	text_tagged = pos_tag(words_lemm)
	#print (text_tagged)

	stopset = set(stopwords.words('english')) - set(('over', 'under', 'below', 'more', 'most', 'no', 'not', 'only',
													 'such', 'few', 'so', 'too', 'very', 'just', 'any', 'once'))
	from nltk.corpus import twitter_samples
	print (stopset)

	pos_tweets = twitter_samples.strings('positive_tweets.json')
	print (pos_tweets)

	neg_tweets = twitter_samples.strings('negative_tweets.json')
	print (neg_tweets)

	if (len(pos_tweets) == len(neg_tweets)):
		print ("Same length")
	else:
		print ("Different lengths")

#--
#--

sent_ext()

