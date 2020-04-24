#!/usr/bin/python

import re
import editdistance
import string
import csv
from collections import Counter

def tokenize(words):
	# finds all words in text file and change everything to lower case
	return re.findall('[a-z]+', words.lower())

# Create dictionary from corpus
Dictionary = Counter(tokenize(open('mobydick.txt').read())) + Counter(tokenize(open('big.txt').read()))

Numwords = sum(Dictionary.values())

#probability of a word
def p(word):
	return Dictionary[word] / Numwords

#All words that are 1 distance away
def dist1(word):
    one_array = []
    for words in Dictionary:
    	if editdistance.eval(word, words) == 1:
    		one_array.append(words)
    return one_array

#2 distance away
def dist2(word):
	one_array = []
	# for d1 in dist1(word):
	# 	for d2 in dist1(d1):
	# 		one_array.append(d2)
	for words in Dictionary:
		if editdistance.eval(word, words) == 2:
			one_array.append(words)
	return one_array

def dist3(word):
	one_array = []
	# for d1 in dist1(word):
	# 	for d2 in dist1(d1):
	# 		for d3 in dist1(d2):
	# 			one_array.append(d3)
	for words in Dictionary:
		if editdistance.eval(word, words) == 3:
			one_array.append(words)
	return one_array

#Choose candidates of words starting from distance of 1
def candidates(word):
	candidate = []
	if len(dist1(word)) > 0:
		candidate = dist1(word)
	elif len(dist2(word)) > 0:
		candidate = dist2(word)
	else:
		candidate = dist3(word)

	return sorted(candidate, key=p, reverse=True)[:3]

#Check the list of words
def checkword(text):
	print("List of incorrect words\n")

	Wordslist = Counter(tokenize(open(text).read()))

	for i in Wordslist:
		if i not in Dictionary:
			print(i, ": ", candidates(i))

checkword("input.txt")