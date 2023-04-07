import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
import cv2
from easygui import *
import os
from PIL import Image, ImageTk
from itertools import count
import tkinter as tk
import string
from youtube_transcript_api import YouTubeTranscriptApi
import pickle
from sklearn.feature_extraction.text import CountVectorizer
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from tkinter import messagebox

#import selecting
# obtain audio from the microphone
def func():
        r = sr.Recognizer()
        isl_gif=['good afternoon', 'good morning', 'i am sorry', 'i am tired', 'nice to meet you', 'what is your name']
        
        
        arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        with sr.Microphone() as source:
                # image   = "signlang.png"
                # msg="HEARING IMPAIRMENT ASSISTANT"
                # choices = ["Live Voice","All Done!"] 
                # reply   = buttonbox(msg,image=image,choices=choices)
                r.adjust_for_ambient_noise(source) 
                i=0
                while True:
                        print("I am Listening")
                        audio = r.listen(source)
                        # recognize speech using Sphinx
                        try:
                                a=r.recognize_google(audio)
                                file = open("transcript.txt", "a")
                                file.write("\n"+ a)
                                file.close()
                                a = a.lower()
                                print('You Said: ' + a.lower())
                                
                                for c in string.punctuation:
                                    a= a.replace(c,"")
                                    
                                if(a.lower()=='goodbye' or a.lower()=='good bye' or a.lower()=='bye'):
                                        print("oops!Time To say good bye")
                                        break
                                
                                elif(a.lower() in isl_gif):
                                    
                                    class ImageLabel(tk.Label):
                                            """a label that displays images, and plays them if they are gifs"""
                                            def load(self, im):
                                                if isinstance(im, str):
                                                    im = Image.open(im)
                                                self.loc = 0
                                                self.frames = []

                                                try:
                                                    for i in count(1):
                                                        self.frames.append(ImageTk.PhotoImage(im.copy()))
                                                        im.seek(i)
                                                except EOFError:
                                                    pass

                                                try:
                                                    self.delay = im.info['duration']
                                                except:
                                                    self.delay = 100

                                                if len(self.frames) == 1:
                                                    self.config(image=self.frames[0])
                                                else:
                                                    self.next_frame()

                                            def unload(self):
                                                self.config(image=None)
                                                self.frames = None

                                            def next_frame(self):
                                                if self.frames:
                                                    self.loc += 1
                                                    self.loc %= len(self.frames)
                                                    self.config(image=self.frames[self.loc])
                                                    self.after(self.delay, self.next_frame)
                                    root = tk.Tk()
                                    lbl = ImageLabel(root)
                                    lbl.pack()
                                    lbl.load(r'Gifs/{0}.gif'.format(a.lower()))
                                    root.mainloop()
                                else:
                                    for i in range(len(a)):
                                                    if(a[i] in arr):
                                            
                                                            ImageAddress = 'letters/'+a[i]+'.jpg'
                                                            ImageItself = Image.open(ImageAddress)
                                                            ImageNumpyFormat = np.asarray(ImageItself)
                                                            plt.imshow(ImageNumpyFormat)
                                                            plt.draw()
                                                            plt.pause(0.5)
                                                    else:
                                                            continue

                        except:
                               print(" ")
                        plt.close()


def yt_trans(id):
    trans = YouTubeTranscriptApi.get_transcript(id, languages=['en'])
# print(trans)


    print('===========================')
    to_remove = {'\\xa0':""}

    for i in to_remove.keys():
        trans1= str(trans).replace(i,to_remove[i])
    # print(trans1)
    file = open('trans(using_module).txt',"w")
    file.write(str(trans1))
    file.close()


    # with open('trans(using_module)2.pkl', 'wb') as fp:
    # # file = open('trans(using_module)2.pkl',"wb")
    #     pickle.dump(trans1,fp)
    # # file.close()


    trans = YouTubeTranscriptApi.get_transcript('ArFQdvF8vDE', languages=['en'])
    outls = []
    for i in trans:
        outtxt = i['text']
        outls.append(outtxt)
        with open('op.txt',"a") as opf:
            opf.write(outtxt + '\n')

    vectorizer = CountVectorizer()

    vectorizer.fit(outls)

    print('Vocab : ', vectorizer.vocabulary_)

    def listToString(s):
    
        # initialize an empty string
        str1 = ""

        # traverse in the string
        for ele in s:
            str1 += ele

        # return string
        return str1

    arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r', 's','t','u','v','w','x','y','z']
    
    with open ('op.txt', "r") as myfile:
        listofsent=myfile.readlines() 

        a = listToString(listofsent)
    for i in (str(a)):
        if(i in arr):

                ImageAddress = 'letters/'+ i +'.jpg'
                ImageItself = Image.open(ImageAddress)
                ImageNumpyFormat = np.asarray(ImageItself)
                plt.imshow(ImageNumpyFormat)
                print(i)
                plt.draw()
                plt.pause(0.5)
        else:
                continue
    print("-------------------------------------------")

    
    def summarize():
        
        # text = trans1
        # Input text - to summarize
        with open ('op.txt', "r") as myfile:
            listofsent=myfile.readlines() 

        text = listToString(listofsent)
        print("length of text is : ",len(text))    
        print(text + "\n====================================")
        stopWords = set(stopwords.words("english"))
        words = word_tokenize(text)
        
        # Creating a frequency table to keep the 
        # score of each word
        
        freqTable = dict()
        for word in words:
            word = word.lower()
            if word in stopWords:
                continue
            if word in freqTable:
                freqTable[word] += 1
            else:
                freqTable[word] = 1
        
        # Creating a dictionary to keep the score
        # of each sentence
        sentences = sent_tokenize(text)
        sentenceValue = dict()
        
        for sentence in sentences:
            for word, freq in freqTable.items():
                if word in sentence.lower():
                    if sentence in sentenceValue:
                        sentenceValue[sentence] += freq
                    else:
                        sentenceValue[sentence] = freq
        
        
        
        sumValues = 0
        for sentence in sentenceValue:
            sumValues += sentenceValue[sentence]
        
        # Average value of a sentence from the original text
        
        average = int(sumValues / len(sentenceValue))
        
        # Storing sentences into our summary.
        summary = ''
        for sentence in sentences:
            if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
                summary += " " + sentence
        # print("summary is : ", summary)
    # Python program to convert a list to string

    # Function to convert


    

    # Driver code
    summarize()


while 1:
  image   = "signlang.png"
  msg="HEARING IMPAIRMENT ASSISTANT"
  choices = ["Live Voice","All Done!","Youtube transcript"] 
  reply   = buttonbox(msg,image=image,choices=choices)
  id = enterbox("Enter the youtube id : ","youtube id")
  if reply ==choices[0]:
        func()
  if reply == choices[1]:
        quit()
  if reply == choices[2]:
        yt_trans(id)
        messagebox.Message('Your transcript has been saved')
        
