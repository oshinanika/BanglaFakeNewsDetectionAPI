# Reference: https://pypi.org/project/face-recognition/
import face_recognition
from pathlib import Path
from PIL import Image
from pytesseract import Output
import json
from cv2 import cv2
import re

from mlapp import app
import mlapp.services.logs as logger
import base64
import os
import pytesseract


from passporteye import read_mrz

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

#=============

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


import tensorflow as tf
import pandas as pd
import numpy as np

import nltk
import re
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords as stop_words
from nltk.tokenize import word_tokenize, sent_tokenize
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS

#LSTM MODEL
from tensorflow.keras.preprocessing.text import one_hot, Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Embedding, Input, LSTM, Conv1D, MaxPool1D, Bidirectional
from tensorflow.keras.models import Model

#Bangla NLP
from bnlp.corpus import stopwords, punctuations
from bnlp.corpus.util import remove_stopwords
from bnlp import NLTKTokenizer
from nltk import word_tokenize
bnltk = NLTKTokenizer()

# split data into test and train 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score



# visualize the distribution of number of words in a text
#import plotly.express as px

#the confusion matrix
#from sklearn.metrics import confusion_matrix
#==============
#nltk.download('punkt')
class ExtractInfo:
    __root_path = app.config.get("DIR_STATIC")
    __dataset_path = app.config.get("DATASET_PATH")

    def getTrueNewsSet(self):
        logger.error_logs("====getTrueNewsSet")
        dataset_path = '{}/Authentic-48K.csv'.format(
                self.__dataset_path)
        try:
            df_true = pd.read_csv(dataset_path)
            df_true = df_true.head(1299)
            return df_true

        except Exception as e:
            logger.error_logs(e)
            return None

    def getFakeNewsSet(self):
        logger.error_logs("====getFakeNewsSet")
        dataset_path = '{}/Fake-1K.csv'.format(
                self.__dataset_path)
        try:
            df_fake = pd.read_csv(dataset_path)

            return df_fake

        except Exception as e:
            logger.error_logs(e)
            return None

    def getCleanedDataset(self):
        logger.error_logs("====getCleanedDataset")
        dataset_path = '{}/BanFakeNews_df_clean_joined50-50.csv'.format(
                self.__dataset_path)
        try:
            df_clean = pd.read_csv(dataset_path)

            return df_clean

        except Exception as e:
            logger.error_logs(e)
            return None

    def preprocess(self, text):
        logger.error_logs("====preprocess")
        logger.error_logs(text)
        try:

            result = []
            for token in bnltk.word_tokenize(text):
                if token not in stop_words and token not in punctuations:
                    result.append(token)
                    
            return result

        except Exception as e:
            logger.error_logs(e)
            return None

    def totalWords(self, df):
        logger.error_logs("====totalWords")
        
        try:

            list_of_words = []
            for i in df.clean:
                for j in i:
                    list_of_words.append(j)

            
            total_words = len(list(set(list_of_words)))
            logger.error_logs(total_words)
            return total_words
        except Exception as e:
            logger.error_logs(e)
            return None

    def maxLen(self, df):
        logger.error_logs("====maxLen")
        
        try:

            maxlen = -1
            for doc in df.clean_joined:
                tokens = bnltk.word_tokenize(doc)
                if(maxlen<len(tokens)):
                    maxlen = len(tokens)
                    #logger.error_logs(maxlen)
                   

            logger.error_logs(maxlen)

            return maxlen

        except Exception as e:
            logger.error_logs(e)
            return None
    
    def dataSetsplit(self, df):
        logger.error_logs("====dataSetsplit")
        
        try:

            x_train, x_test, y_train, y_test = train_test_split(df.clean_joined, df.label, test_size = 0.2)
            #logger.error_logs()

            return x_train, x_test, y_train, y_test

        except Exception as e:
            logger.error_logs(e)
            return None

    def textTokenizer(self, total_words):
        logger.error_logs("====textTokenizer")
        
        try:

            tokenizer = Tokenizer(num_words = total_words)
            logger.error_logs(total_words)

            return tokenizer

        except Exception as e:
            logger.error_logs(e)
            return None

    def fitOnTexts(self, x_train,tokenizer):
        logger.error_logs("====fitOnTexts")
        
        try:

            tokenizer.fit_on_texts(x_train)
            #logger.error_logs()

            return tokenizer

        except Exception as e:
            logger.error_logs(e)
            return None

    def textSequences(self, data, tokenizer):
        logger.error_logs("====textSequences")
        
        try:

            sequences = tokenizer.texts_to_sequences(data)
            #logger.error_logs()

            return sequences

        except Exception as e:
            logger.error_logs(e)
            return None

    def padSequences(self, data_sequences, tokenizer):
        logger.error_logs("====padSequences")
        
        try:

            padded_data = pad_sequences(data_sequences,maxlen = 40, padding = 'post', truncating = 'post')
            #logger.error_logs()

            return padded_data

        except Exception as e:
            logger.error_logs(e)
            return None

    def getNumpyLabel(self, y_train):
        logger.error_logs("====getNumpyLabel")
        
        try:

            y_train = np.asarray(y_train)
            #logger.error_logs()

            return y_train

        except Exception as e:
            logger.error_logs(e)
            return None





    def model_LSTM(self,total_words):
        logger.error_logs("====model_LSTM")
        
        try:

            # Sequential Model
            model = Sequential()

            # embeddidng layer
            model.add(Embedding(total_words, output_dim = 128))
            

            # Bi-Directional RNN and LSTM
            model.add(Bidirectional(LSTM(128)))

            # Dense layers
            model.add(Dense(128, activation = 'relu'))
            model.add(Dense(1,activation= 'sigmoid'))
            model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])
            #model.summary()

            return model

        except Exception as e:
            logger.error_logs(e)
            return None

    def model_LSTM_fit(self, model, padded_train, y_train):
        logger.error_logs("====model_LSTM_fit")
        
        try:

            # train the model
            model.fit(padded_train, y_train, batch_size = 64, validation_split = 0.1, epochs = 2)
            #logger.error_logs()

            return model

        except Exception as e:
            logger.error_logs(e)
            return None

    def model_LSTM_fit_custom_epoch(self, model, padded_train, y_train, epoch):
        logger.error_logs("====model_LSTM_fit")
        
        try:

            # train the model
            model.fit(padded_train, y_train, batch_size = 64, validation_split = 0.1, epochs = int(epoch))
            #logger.error_logs()

            return model

        except Exception as e:
            logger.error_logs(e)
            return None
    def model_LSTM_predict(self, model, padded_test):
        logger.error_logs("====model_LSTM_predict")
        
        try:

            # make prediction
            pred = model.predict(padded_test)
            #logger.error_logs()
            # if the predicted value is >0.5 it is real else it is fake
            prediction = []
            for i in range(len(pred)):
                if pred[i].item() > 0.5:
                    prediction.append(1)
                else:
                    prediction.append(0)
            return prediction

        except Exception as e:
            logger.error_logs(e)
            return None

    def model_Accuracy(self, y_test, prediction):
        logger.error_logs("====model_Accuracy")
        
        try:

            accuracy = accuracy_score(list(y_test), prediction)
            return accuracy

        except Exception as e:
            logger.error_logs(e)
            return None

    def test(self):
        logger.error_logs("====test")
        try:
            df = self.getCleanedDataset()

            #logger.error_logs(df.info())

            #res = self.maxLen(df)
            total_words = self.totalWords(df)
            x_train, x_test, y_train, y_test = self.dataSetsplit(df)
            logger.error_logs("y_train="+str(y_train[0]))

            tokenizer = self.textTokenizer(total_words)
            tokenizer = self.fitOnTexts(x_train, tokenizer)
            train_sequences = self.textSequences(x_train, tokenizer)
            test_sequences = self.textSequences(x_test, tokenizer)
            padded_train = self.padSequences(train_sequences, tokenizer)
            padded_test = self.padSequences(test_sequences, tokenizer)

            logger.error_logs("The encoding for document"+str(len(df.clean_joined[0]))+"\n is : "+str(len(test_sequences[0])))

            model = self.model_LSTM(total_words)
            y_train=self.getNumpyLabel(y_train)
            model = self.model_LSTM_fit(model, padded_train, y_train)
            prediction = self.model_LSTM_predict(model, padded_test)

            logger.error_logs("prediction_length: "+str(len(prediction)))

            accuracy = self.model_Accuracy(y_test, prediction)

            df_true = self.getTrueNewsSet()

            #df_true = df_true.head(1)
            #df_true_info = df_true.info()
            out = df_true.to_json(orient='records')

            #return str(accuracy)
            return out
        except Exception as e:
            logger.error_logs(e)
            return None

    def testSentence(self, testdata):
        logger.error_logs("====testSentence")
        try:
            df = self.getCleanedDataset()

            #logger.error_logs(df.info())

            #res = self.maxLen(df)
            total_words = self.totalWords(df)
            x_train, x_test, y_train, y_test = self.dataSetsplit(df)
            #logger.error_logs("y_train="+str(y_train[0]))

            tokenizer = self.textTokenizer(total_words)
            tokenizer = self.fitOnTexts(x_train, tokenizer)
            train_sequences = self.textSequences(x_train, tokenizer)
            #test_sequences = self.textSequences(x_test, tokenizer)
            padded_train = self.padSequences(train_sequences, tokenizer)
            ##padded_test = self.padSequences(test_sequences, tokenizer)

            #logger.error_logs("The encoding for document"+str(len(df.clean_joined[0]))+"\n is : "+str(len(test_sequences[0])))

            model = self.model_LSTM(total_words)
            y_train=self.getNumpyLabel(y_train)
            model = self.model_LSTM_fit(model, padded_train, y_train)
            #prediction = self.model_LSTM_predict(model, padded_test)

            #logger.error_logs("prediction_length: "+str(len(prediction)))

            #accuracy = self.model_Accuracy(y_test, prediction)

            #custom data
            
            x_test1 = [testdata]
            #x_test1 = self.preprocess(x_test1)
            test_sequences = self.textSequences(x_test1, tokenizer)
            padded_test = self.padSequences(test_sequences, tokenizer)
            prediction = self.model_LSTM_predict(model, padded_test) 

            #logger.error_logs("test data prediction_length: "+str(len(prediction)))
            string_prediction =""
             # traverse in the string  
            for ele in prediction: 
                if ele == 1:
                    string_prediction += 'True' 
                else:
                    string_prediction += 'Fake'
                #string_prediction += str(ele)                       
            return string_prediction

        except Exception as e:
            logger.error_logs(e)
            return None


    def testSentence_customepoch(self, testdata, epoch):
        logger.error_logs("====testSentence")
        try:
            df = self.getCleanedDataset()

            #logger.error_logs(df.info())

            #res = self.maxLen(df)
            total_words = self.totalWords(df)
            x_train, x_test, y_train, y_test = self.dataSetsplit(df)
            logger.error_logs("y_train="+str(y_train[0]))

            tokenizer = self.textTokenizer(total_words)
            tokenizer = self.fitOnTexts(x_train, tokenizer)
            train_sequences = self.textSequences(x_train, tokenizer)
            #test_sequences = self.textSequences(x_test, tokenizer)
            padded_train = self.padSequences(train_sequences, tokenizer)
            ##padded_test = self.padSequences(test_sequences, tokenizer)

            #logger.error_logs("The encoding for document"+str(len(df.clean_joined[0]))+"\n is : "+str(len(test_sequences[0])))

            model = self.model_LSTM(total_words)
            y_train=self.getNumpyLabel(y_train)
            model = self.model_LSTM_fit_custom_epoch(model, padded_train, y_train, epoch)
            #prediction = self.model_LSTM_predict(model, padded_test)

            #logger.error_logs("prediction_length: "+str(len(prediction)))

            #accuracy = self.model_Accuracy(y_test, prediction)

            #custom data
            x_test1 = [testdata]
            test_sequences = self.textSequences(x_test1, tokenizer)
            padded_test = self.padSequences(test_sequences, tokenizer)
            prediction = self.model_LSTM_predict(model, padded_test) 

            logger.error_logs("test data prediction_length: "+str(len(prediction)))
            string_prediction =""
             # traverse in the string  
            for ele in prediction: 
                if ele == 1:
                    string_prediction += 'True' 
                else:
                    string_prediction += 'Fake'
                #string_prediction += str(ele)                       
            return string_prediction

        except Exception as e:
            logger.error_logs(e)
            return None



    def modelAccuracy(self):
        logger.error_logs("====test")
        try:
            df = self.getCleanedDataset()

            #logger.error_logs(df.info())

            #res = self.maxLen(df)
            total_words = self.totalWords(df)
            x_train, x_test, y_train, y_test = self.dataSetsplit(df)
            logger.error_logs("y_train="+str(y_train[0]))

            tokenizer = self.textTokenizer(total_words)
            tokenizer = self.fitOnTexts(x_train, tokenizer)
            train_sequences = self.textSequences(x_train, tokenizer)
            test_sequences = self.textSequences(x_test, tokenizer)
            padded_train = self.padSequences(train_sequences, tokenizer)
            padded_test = self.padSequences(test_sequences, tokenizer)

            logger.error_logs("The encoding for document"+str(len(df.clean_joined[0]))+"\n is : "+str(len(test_sequences[0])))

            model = self.model_LSTM(total_words)
            y_train=self.getNumpyLabel(y_train)
            model = self.model_LSTM_fit(model, padded_train, y_train)
            prediction = self.model_LSTM_predict(model, padded_test)

            logger.error_logs("prediction_length: "+str(len(prediction)))

            accuracy = self.model_Accuracy(y_test, prediction)

            
            return str(accuracy)
            #return out
        except Exception as e:
            logger.error_logs(e)
            return None

    def SampleTrueSet(self):
        logger.error_logs("====SampleTrueSet")
        try:

           
            df_true = self.getTrueNewsSet()

            df_true = df_true.head(5)
            #df_true = df_true.apply(lambda x : str(x).encode('raw_unicode_escape'))
            #df_true_info = df_true.info()
            #out = df_true.to_json(orient='records')
            out=df_true.to_dict(orient='records')
            #return str(accuracy)
            return out
        except Exception as e:
            logger.error_logs(e)
            return None
    
    def SampleFakeSet(self):
        logger.error_logs("====SampleFakeSet")
        try:

           
            df_true = self.getFakeNewsSet()

            df_true = df_true.head(5)
            #df_true_info = df_true.info()
            out = df_true.to_dict(orient='records')

            #return str(accuracy)
            return out
        except Exception as e:
            logger.error_logs(e)
            return None

    def totalUniqueDomains(self):
        logger.error_logs("====totalUniqueDomains")
        try:

           
            df = self.getCleanedDataset()
            total_domain = sorted(list(set(df['domain'])))

            # string_prediction =""
            #  # traverse in the string  
            # for ele in total_domain: 
                
            #         string_prediction += ele 
                
            #         string_prediction += 'Fake'
            #     #string_prediction += str(ele) 

            #list1 = [1, 2, 3]
            #str1 = ','.join(str(e) for e in total_domain)
            return str(total_domain)
            #return str1
        except Exception as e:
            logger.error_logs(e)
            return None

    def totalUniqueCategory(self):
        logger.error_logs("====totalUniqueCategory")
        try:

           
            df = self.getCleanedDataset()
            total_domain = sorted(list(set(df['category'])))

            # string_prediction =""
            #  # traverse in the string  
            # for ele in total_domain: 
                
            #         string_prediction += ele 
                
            #         string_prediction += 'Fake'
            #     #string_prediction += str(ele) 

            #list1 = [1, 2, 3]
            #str1 = ','.join(str(e) for e in total_domain)
            return str(total_domain)
            #return str1
        except Exception as e:
            logger.error_logs(e)
            return None
   

   