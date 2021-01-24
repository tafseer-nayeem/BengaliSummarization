#Extractive Summarization

import os
import sentTokenizer
import TextRank as textRank
import Clustering_tfidf as clustering

#create folder
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

#convert list into String
def listToString(s):  
    str1 = " "      
    return (str1.join(s)) 

#Get Summary
def getSummary(filename):  
    summary = []
    for k in range(n):
        summary_lines = textRank.extract_summary(filename[k])
        summary.append(summary_lines)
    full_summary =[]
    for x in summary:
        left_text = x.partition("।")[0]
        left_text = left_text.partition("?")[0]
        left_text = left_text.partition("!")[0]
        full_summary.append(left_text+"।")  
    s = listToString(full_summary)
    si = sentTokenizer.sentTokenizing().sentTokenize(s)
    summ = sentence_ordering(si)
    return summ

#Sentence ordering
def sentence_ordering(unordered_summary):
    unordered_summary = [x[:(len(x)-1)].strip(' ') for x in unordered_summary]
    docs = [x[:(len(x)-1)].strip(' ') for x in doc]
    both = set(docs).intersection(unordered_summary)
    indices_A = [docs.index(x) for x in both]
    indices_B = [unordered_summary.index(x) for x in both]    
    dictionary = {}
    for x in range(len(indices_A)):
        dictionary[indices_A[x]] = indices_B[x]    
    ordered_summary = []
    for i in sorted (dictionary) : 
        ordered_summary.append(dictionary[i])
    st =""
    for i in ordered_summary:
        st = st +(unordered_summary[i])+'। '
    return st  

"""
for i in range(1,101):
    serial_no = str(i)
    document = open('DataSet/BNLPC/Dataset1/NormaliseDocument/Document_'+serial_no+'.txt').read()
    doc = sentTokenizer.sentTokenizing().sentTokenize(document)
    filenamee, n = clustering.startF(doc)
    summary = getSummary(filenamee)
    #save the summary
    createFolder('DataSet/BNLPC/Dataset1/MachineGeneratedSummaryNew/')
    fi = open('DataSet/BNLPC/Dataset1/MachineGeneratedSummaryNew/'+serial_no+'.txt','+w')
    fi.write(summary)
"""