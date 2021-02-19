#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function
from collections import defaultdict
from pythonrouge.pythonrouge import Pythonrouge
from pprint import pprint


serialList = []
for i in range(1,140):
    serialList.append(i)

def word2ids(summary, reference):
    id_dict = defaultdict(lambda: len(id_dict))
    summary = [[' '.join([str(id_dict[w]) for w in sent.split()])
                for sent in doc] for doc in summary]
    reference = [[[' '.join([str(id_dict[w]) for w in sent.split()])
                   for sent in doc] for doc in refs] for refs in reference]
    return summary, reference


def getsummary():
    summary = []
    for i in serialList:
        a = str(i)
        fmachine = open("baselineAlgorithm/Dataset/NCTB/KlSummary/"+a+".txt","r").read()
        s = fmachine.split('।')
        for i in range(len(s)):
            s[i] = s[i] + '.'
        s.pop()
        s = [x.strip(' ') for x in s]
        summary.append(s)
    return summary

def getreference():
    reference = []
    for i in serialList:
        a = str(i)
        fmachine = open("Dataset/NCTB/Summary/"+a+".txt","r").read()
        s = fmachine.split('।')
        for i in range(len(s)):
            s[i] = s[i] + '.'
        s.pop()
        s = [x.strip(' ') for x in s]
        reference.append(s)
        
    r = [[i] for i in reference] #2d to 3d
    return r


if __name__ == '__main__':
    # prediction
    
    #getsummary
    summary = getsummary()
    print(summary)
    
    #getreference
    reference = getreference()
    print(reference)

    summary, reference = word2ids(summary, reference)
    rouge = Pythonrouge(summary_file_exist=False,
                        summary=summary, reference=reference,
                        n_gram=2, ROUGE_SU4=True, ROUGE_L=True,
                        recall_only=False)
    score = rouge.calc_score()
    print('ROUGE-N(1-2) & SU4 recall only')
    pprint(score)



