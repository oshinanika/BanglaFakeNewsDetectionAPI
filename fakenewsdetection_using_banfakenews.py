# -*- coding: utf-8 -*-
"""FakeNewsDetection using BanFakeNews-Coursera.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14UvZ39QePPCN4vqgog7cjLtTIXpsSEWF
"""
"""
Dependencies
!pip install --upgrade tensorflow-gpu==2.0

!pip install plotly
!pip install --upgrade nbformat
!pip install nltk
!pip install spacy # spaCy is an open-source software library for advanced natural language processing
!pip install WordCloud
!pip install bnlp_toolkit
!pip install gensim # Gensim is an open-source library for unsupervised topic modeling and natural language processing
!pip install jupyterthemes
"""
# import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import nltk
import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from wordcloud import WordCloud, STOPWORDS
import nltk
import re
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
# import keras
from tensorflow.keras.preprocessing.text import one_hot, Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Embedding, Input, LSTM, Conv1D, MaxPool1D, Bidirectional
from tensorflow.keras.models import Model

from bnlp.corpus import stopwords, punctuations
from bnlp.corpus.util import remove_stopwords
from bnlp import NLTKTokenizer


# split data into test and train 
from sklearn.model_selection import train_test_split

from bnlp import NLTKTokenizer
from nltk import word_tokenize

# visualize the distribution of number of words in a text
import plotly.express as px

#the accuracy
from sklearn.metrics import accuracy_score
#the confusion matrix
from sklearn.metrics import confusion_matrix



nltk.download('punkt')


# from google.colab import drive
# drive.mount('/content/drive')

# load the data
df_true = pd.read_csv("F:\\AnikaOshin\\FINAL\\BanglaFakeNewsDetectionAPI\\BanFakeNewsDataset\\BanFakeNews\\Authentic-48K.csv")
df_fake = pd.read_csv("F:\\AnikaOshin\\FINAL\\BanglaFakeNewsDetectionAPI\\BanFakeNewsDataset\\BanFakeNews\\Fake-1K.csv")

df_true

df_fake

df_true.isnull().sum()

df_fake.isnull().sum()

df_true.info()

df_fake.info()

# Concatenate Real and Fake News
df = pd.concat([df_true, df_fake]).reset_index(drop = True)
df

df.drop(columns = ['date'], inplace = True)

df['original'] = df['headline'] + ' ' + df['content']
df.head()

raw_text = df['original'][0]



stop_words = stopwords
punctuations = punctuations
punctuations


result = remove_stopwords(raw_text, stop_words)
print(result)

# Remove stopwords and remove words with 2 or less characters


bnltk = NLTKTokenizer()

def preprocess(text):
    result = []
    for token in bnltk.word_tokenize(text):
        if token not in stop_words and token not in punctuations:
            result.append(token)
            
    return result

#=======================================================================================
# Apply the function to the dataframe
df['clean'] = df['original'].apply(preprocess)
#=======================================================================================
# Show cleaned up news after removing stopwords
print(df['clean'][0])

#=======================================================================================
# Obtain the total words present in the dataset
list_of_words = []
for i in df.clean:
    for j in i:
        list_of_words.append(j)

list_of_words

len(list_of_words)

# Obtain the total number of unique words
total_words = len(list(set(list_of_words)))
total_words
#=======================================================================================
# join the words into a string
df['clean_joined'] = df['clean'].apply(lambda x: " ".join(x))

df

df['clean_joined'][0]

plt.figure(figsize = (8, 8))
sns.countplot(y = "category", data = df)

plt.figure(figsize = (8, 8))
sns.countplot(y = "label", data = df)

#=======================================================================================
# length of maximum document will be needed to create word embeddings 
maxlen = -1
for doc in df.clean_joined:
    tokens = bnltk.word_tokenize(doc)
    if(maxlen<len(tokens)):
        maxlen = len(tokens)
print("The maximum number of words in any document is =", maxlen)
#=======================================================================================


#split data into test train
fig = px.histogram(x = [len(bnltk.word_tokenize(x)) for x in df.clean_joined], nbins = 100)
fig.show()

#=======================================================================================
x_train, x_test, y_train, y_test = train_test_split(df.clean_joined, df.label, test_size = 0.2)
#=======================================================================================

plt.figure(figsize = (8, 8))
sns.countplot(y = "label", data = df)



bnltk = NLTKTokenizer()
bnltk


tokenizer = Tokenizer(num_words = total_words)
tokenizer

#=======================================================================================
# Create a tokenizer to tokenize the words and create sequences of tokenized words
tokenizer = Tokenizer(num_words = total_words)
tokenizer.fit_on_texts(x_train)
train_sequences = tokenizer.texts_to_sequences(x_train)
test_sequences = tokenizer.texts_to_sequences(x_test)
#=======================================================================================

print("The encoding for document\n",df.clean_joined[0],"\n is : ",train_sequences[0])

#=======================================================================================
# Add padding can either be maxlen = 4406 or smaller number maxlen = 40 seems to work well based on results
padded_train = pad_sequences(train_sequences,maxlen = 40, padding = 'post', truncating = 'post')
padded_test = pad_sequences(test_sequences,maxlen = 40, truncating = 'post')
#=======================================================================================

for i,doc in enumerate(padded_train[:2]):
     print("The padded encoding for document",i+1," is : ",doc)

#=======================================================================================
# Sequential Model
model = Sequential()

# embeddidng layer
model.add(Embedding(total_words, output_dim = 128))
# model.add(Embedding(total_words, output_dim = 240))


# Bi-Directional RNN and LSTM
model.add(Bidirectional(LSTM(128)))

# Dense layers
model.add(Dense(128, activation = 'relu'))
model.add(Dense(1,activation= 'sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])
model.summary()
#=======================================================================================
total_words

y_train = np.asarray(y_train)
#=======================================================================================
# train the model
model.fit(padded_train, y_train, batch_size = 64, validation_split = 0.1, epochs = 2)
#=======================================================================================

#=======================================================================================
# make prediction
pred = model.predict(padded_test)
#=======================================================================================

# if the predicted value is >0.5 it is real else it is fake
prediction = []
for i in range(len(pred)):
    if pred[i].item() > 0.5:
        prediction.append(1)
    else:
        prediction.append(0)

#=======================================================================================
# getting the accuracy

#=======================================================================================
accuracy = accuracy_score(list(y_test), prediction)

print("Model Accuracy : ", accuracy)

# get the confusion matrix

cm = confusion_matrix(list(y_test), prediction)
plt.figure(figsize = (25, 25))
sns.heatmap(cm, annot = True)

# category dict
category = { 0: 'Fake News', 1 : "Real News"}

# data containing real news
df_true
# data containing fake news
df_fake
# dataframe information
df_true.info()
# dataframe information
df_fake.info()
# check for null values
df_true.isnull().sum()
# check for null values
df_fake.isnull().sum()

df['original'][5]
df['clean_joined'][5]

# plot the number of samples per each class
plt.figure(figsize = (8, 8))
sns.countplot(y = "label", data = df)