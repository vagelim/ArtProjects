#dataset from grocery.com
#converted excel to csv
#imported the csv and wrote it to a pickle for easier access

#import the pickle grocery.pickle
#read it in
#Take an input string

#For each word in string, find a product it can be found in
	#The word is a substring of a product name
import pickle
import random
grocery = pickle.load( open('grocery.pickle', 'rb') )

t = raw_input('Enter your string: ')
products = []
t = t.split()
print "Input size: " + str(len(t))
for each in t:
	count = 0
	possible = []
	while count < len(grocery):
		if str(grocery[count]).find(each) != -1:
			possible.append(grocery[count])
		count += 1
	try:
		products.append(random.choice(possible))
	except IndexError:
		#There will be an exception if the word is not found
		#Find a synonym and try that word
		#TODO
		print "Word: " + each + " not found."

print products
print len(products)



def syn(word): #synonym function
	import nltk
	from nltk.corpus import wordnet as wn
	syns = wn.synsets(word)
	syns = [l.name for s in syns for l in s.lemmas]
	