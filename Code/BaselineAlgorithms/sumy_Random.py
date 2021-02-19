#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.random import RandomSummarizer as Summarizer
from sumy.utils import get_stop_words
from sumy.nlp.stemmers import Stemmer
from sumy.nlp.tokenizers import Tokenizer
from wordConverter import word
import os
#create folder
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)


LANGUAGE = "bangla"
SENTENCES_COUNT = 2

if __name__ == "__main__":

    createFolder('Dataset/NCTB/RandomSummary/')
    for i in range(1,140):
        serial_no = str(i)
        path = "Dataset/NCTB/Source/" + serial_no + ".txt"
        parser = PlaintextParser.from_file(path, Tokenizer(LANGUAGE))
        stemmer = Stemmer(LANGUAGE)
        summarizer = Summarizer(stemmer)
        summarizer.stop_words = get_stop_words(LANGUAGE)
        summary = ""
        for sentence in summarizer(parser.document, SENTENCES_COUNT):
            summary = summary+ " "+str(sentence)
        fi = open('Dataset/NCTB/RandomSummary/'+serial_no+'.txt','+w')
        fi.write(summary)

    
