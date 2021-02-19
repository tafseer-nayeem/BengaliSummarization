# -*- coding: utf-8 -*-

"""
To spllit a sentence into words,you must need to import sentTokenizer because here 
some tasks are done to make data flexible so that wordConverter.py can give
words properly.So at any where if you want to get words from a sentence,you have to do 
sentence tokenizing.And it can take a sentence not a passage. 
"""
#from sentTokenizer import sentTokenizing
import nltk
class word:
    def sentToWord(self,gettingData):
        cleanSent=''
        for i in gettingData:
            for j in i:
                if j=='”' or j=='“' or j=='"' or j==',' or j=='‘' or j=='’':
                    cleanSent+=' '
                    continue  
                elif j=='!' or j=='?' or j=='।':  
                    cleanSent+=' '
                    continue  
                elif j=='(' or j=='{' or j=='}' or j=='[' or j==']':
                    cleanSent+=' ' 
                else:
                    if j=='-' or j==':' or j==')': 
                        cleanSent+=' '
                    else:
                        cleanSent+=j
        return nltk.word_tokenize(cleanSent)
    
