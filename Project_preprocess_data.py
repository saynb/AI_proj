
import sys, math, re
from operator import itemgetter
import math
import os
import nltk
from colorama import init
from termcolor import colored
import pandas as pd
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve
from sklearn.model_selection import ShuffleSplit
import sklearn.datasets
import sklearn.metrics
import sklearn.svm
import sklearn.naive_bayes
import sklearn.neighbors
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer



print(colored("Where is the dataset ? Specify the path", 'blue', attrs = ['bold']))

path = r'F:\SBU_FirstSem\Artificial_Intelligence\\Project\\train.csv'
print(colored("Path to dataset is \n" + path, 'green', attrs = ['bold']))

class Comment:
    def __init__(self, content):
        self.text = content

inp = open(path, 'r')
inp_header = inp.readline()
header_list = re.split("[,\n]" , inp_header)

print(colored("Path to dataset is \n", 'green', attrs = ['bold']))
print(header_list)

#Reading Dataset
dataframe_dataset = pd.read_csv(path, na_values='unknown')

# The list for the corresponding 1 and 0 values of the comments
dataframe_target = dataframe_dataset[['Insult']]
insult_target = dataframe_target.ix[:,0].tolist()
print(insult_target)

col3 = dataframe_dataset[['Comment']]
# Removing \n
dataframe_dataset['Comment'] = dataframe_dataset['Comment'].str.replace('\n', '')
#print(dataframe_dataset['Comment'])
#example1 = BeautifulSoup(dataframe_dataset['Comment'][0], "lxml")

#print(example1.get_text)
# Removing all HTML Tags
dataframe_dataset['Comment'] = dataframe_dataset['Comment'].str.replace('[^\w\s]','')
#print(dataframe_dataset['Comment'])

# Converting all uppercase letters to lower case
dataframe_dataset['Comment'] = dataframe_dataset['Comment'].str.lower()
#print(dataframe_dataset['Comment'])

#Tokenizing all the words in a given sentence
dataframe_dataset['tokenized_sents'] = dataframe_dataset.apply(lambda row: nltk.word_tokenize(row['Comment']), axis=1)
#print(dataframe_dataset['tokenized_sents'])

#print(dataframe_dataset)

#Removing all the stop words which have no meaning
stop = stopwords.words('english')
#print(stop)
dataframe_dataset['tokenized_sents'] = dataframe_dataset['tokenized_sents'].apply(lambda x: [item for item in x if item not in stop])
#print(dataframe_dataset['tokenized_sents'])

# Stemming all the words
stemmer = SnowballStemmer('english')
dataframe_dataset['stemmed'] = dataframe_dataset["tokenized_sents"].apply(lambda x: [stemmer.stem(y) for y in x])
#print(dataframe_dataset['stemmed'])

#This is the list for all the words
list_of_all_words = []
list_of_all_words = dataframe_dataset['stemmed'].tolist()

# Separating the list of both insulting and non insulting comments
'''for i in dataframe_dataset['Insult']:
    if dataframe_dataset.iloc[i]['Insult'] == 1:

        insulting_list.append(dataframe_dataset['stemmed'])

print(insulting_list)'''
'''dataframe_dataset_filter = dataframe_dataset.loc[dataframe_dataset['Insult'] == 1]
insulting_list = dataframe_dataset_filter['stemmed'].tolist()
print(insulting_list)'''

list_of_all_words = [[x.replace(" u ", " you" ) for x in l] for l in list_of_all_words]
list_of_all_words = [[x.replace(" em "," them ") for x in l] for l in list_of_all_words]
list_of_all_words = [[x.replace(" da "," the ") for x in l] for l in list_of_all_words]
list_of_all_words = [[x.replace(" yo "," you ") for x in l] for l in list_of_all_words]
list_of_all_words = [[x.replace(" ur "," you ") for x in l] for l in list_of_all_words]
list_of_all_words = [[x.replace("won't", "will not") for x in l] for l in list_of_all_words]
list_of_all_words = [[x.replace("can't", "cannot") for x in l] for l in list_of_all_words]
list_of_all_words = [[x.replace("i'm", "i am") for x in l] for l in list_of_all_words]
list_of_all_words = [[x.replace(" im ", " i am ") for x in l] for l in list_of_all_words]
list_of_all_words = [[x.replace("ain't", "is not") for x in l] for l in list_of_all_words]
list_of_all_words = [[x.replace("'ll", " will") for x in l] for l in list_of_all_words]
list_of_all_words = [[x.replace("'t", " not") for x in l] for l in list_of_all_words]
list_of_all_words = [[x.replace("'ve", " have") for x in l] for l in list_of_all_words]
list_of_all_words = [[x.replace("'s", " is") for x in l] for l in list_of_all_words]
list_of_all_words = [[x.replace("'re", " are") for x in l] for l in list_of_all_words]
list_of_all_words = [[x.replace("'d", " would") for x in l] for l in list_of_all_words]

print(list_of_all_words)

#insulting_list_1d =  [x for sublist in insulting_list for x in sublist]

#print(colored("Bag of words built after applying all the above mentioned things are : \n", 'cyan', attrs = ['bold']))

#print(insulting_list_1d)

# Replacing the words which are in slang form 



#print(insulting_list_1d)

# Taking google list of bad words
bw = open('full-list-of-bad-words.txt', 'r')

inp_text = bw.read()  # raeding file generated from puzzleenerator.py
inp_text = re.split('\n|,', inp_text)
#print(inp_text)
 
# Using sklearn features to train the data


# Training
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB

print("Using Naive Baye's")
from sklearn.naive_bayes import MultinomialNB

text_clf = Pipeline([('vect', CountVectorizer(ngram_range=(2, 2))),
                     ('tfidf', TfidfTransformer()),
                     ('clf', MultinomialNB()),
                     ])
print(len(insulting_list_1d))
text_clf = text_clf.fit(insulting_list_1d)

print("Print here the mean value")
from sklearn import metrics
print("Print metric report")
