# -*- coding: utf-8 -*-

"""
Here it takes a paasage/article then do some processing and finally gives spllit
the article/passage into sentences.Then joining all sentences gives a flexible list
of sentences.
"""
'''
import codecs
with codecs.open("S.txt",'r',encoding="utf-8") as myfile:
    text= myfile.read()'''
class sentTokenizing:
    def sentTokenize(self,gettingText):
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
        #print(data)
                
        return data
 
#a=sentTokenizing().sentTokenize(text)
#print(a)
        