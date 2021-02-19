#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nltk
from typing import List
class Tokenizer:

    """
    @staticmethod
    def to_sentences(text: str) -> List[str]:
        return [s.strip() for s in text.split(".")]

    @staticmethod
    def to_words(sentence: str) -> List[str]:
        return [w.strip() for w in sentence.split(" ")]
    """   


    @staticmethod
    def to_sentence(gettingText: str) -> List[str]:
        dataToReSize=[]
        data=[]
        cleanText=''
        for i in gettingText:
            if i=='।' or i=='!' or i=='?':
                cleanText+=i
                dataToReSize.append(''.join(cleanText))
                cleanText=''
            else:
                if i=='\n' or i=='\r' or i=='”' or i=='“' or i=='"':
                    continue
                else:
                    cleanText+=i
        for i in dataToReSize:
            withoutAheadSpace=''
            flag=1
            for j in i:
                if j==' ' and flag:
                    continue
                else:
                    flag=0
                    withoutAheadSpace+=j
            data.append(''.join(withoutAheadSpace))
                
        return data
    
    @staticmethod
    def to_words(gettingData: str) -> List[str]:
        #to_sentence(sentence)
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
        

    
    
    
    
    