#Extractive Summarization
#TextRank

import io
import os
import nltk
import itertools
import editdistance
import networkx as nx
from wordConverter import word
from sentTokenizer import sentTokenizing
word_token = []
stem_words = []
words_pos = []
f = []
p = []

def filter_for_tags(tagged, tags=['NN', 'JJ']):
    """Apply syntactic filters based on POS tags."""
    return [item for item in tagged if item[1] in tags]

def normalize(tagged):
    """Return a list of tuples with the first item's periods removed."""
    return [(item[0].replace('.', ''), item[1]) for item in tagged]

def extract_summary(filename):
    with open(filename) as f:
        #summary = extract_key_phrases(f.read())
        summary = extract_sentences(f.read())
        return summary

def unique_everseen(iterable, key=None):
    """List unique elements in order of appearance.

    Examples:
        unique_everseen('AAAABBBCCDAABBB') --> A B C D
        unique_everseen('ABBCcAD', str.lower) --> A B C D
    """
    seen = set()
    seen_add = seen.add
    if key is None:
        for element in [x for x in iterable if x not in seen]:
            seen_add(element)
            yield element
    else:
        for element in iterable:
            k = key(element)
            if k not in seen:
                seen_add(k)
                yield element


def build_graph(nodes):
    """Return a networkx graph instance.
    :param nodes: List of hashables that represent the nodes of a graph.
    """
    gr = nx.Graph()  # initialize an undirected graph
    gr.add_nodes_from(nodes)
    nodePairs = list(itertools.combinations(nodes, 2))

    # add edges to the graph (weighted by Levenshtein distance)
    for pair in nodePairs:
        firstString = pair[0]
        secondString = pair[1]
        levDistance = editdistance.eval(firstString, secondString)
        gr.add_edge(firstString, secondString, weight=levDistance)
    return gr


def extract_key_phrases(text):
    """Return a set of key phrases.
    :param text: A string.
    """
    tagged = []
    
    # tokenize the text using nltk   
    #word_tokens = nltk.word_tokenize(text)   
    sentence_token = sentTokenizing().sentTokenize(text)
    word_tokens = word().sentToWord(sentence_token)

    # assign POS tags to the words in the text
    tagged = nltk.pos_tag(word_tokens)
    textlist = [x[0] for x in tagged]
    tagged = filter_for_tags(tagged)
    tagged = normalize(tagged)
    unique_word_set = unique_everseen([x[0] for x in tagged])
    word_set_list = list(unique_word_set)

    # this will be used to determine adjacent words in order to construct
    # keyphrases with two words
    graph = build_graph(word_set_list)

    # pageRank - initial value of 1.0, error tolerance of 0,0001,
    calculated_page_rank = nx.pagerank(graph, weight='weight')

    # most important words in ascending order of importance
    keyphrases = sorted(calculated_page_rank, key=calculated_page_rank.get,
                        reverse=True)

    # the number of keyphrases returned will be relative to the size of the
    # text (a third of the number of vertices)
    one_third = len(word_set_list) // 3
    keyphrases = keyphrases[0:one_third + 1]

    # take keyphrases with multiple words into consideration as done in the
    # paper - if two words are adjacent in the text and are selected as
    # keywords, join them together
    modified_key_phrases = set([])
    # keeps track of individual keywords that have been joined to form a keyphrase
    dealt_with = set([])
    i = 0
    j = 1
    while j < len(textlist):
        first = textlist[i]
        second = textlist[j]
        if first in keyphrases and second in keyphrases:
            keyphrase = first + ' ' + second
            modified_key_phrases.add(keyphrase)
            dealt_with.add(first)
            dealt_with.add(second)
        else:
            if first in keyphrases and first not in dealt_with:
                modified_key_phrases.add(first)

            # if this is the last word in the text, and it is a keyword, it
            # definitely has no chance of being a keyphrase at this point
            if j == len(textlist) - 1 and second in keyphrases and \
                    second not in dealt_with:
                modified_key_phrases.add(second)

        i = i + 1
        j = j + 1
    return modified_key_phrases

def extract_sentences(text, summary_length=40, clean_sentences=False, language='bangla'):
    """Return a paragraph formatted summary of the source text.
    :param text: A string.
    """
    sentence_tokens = sentTokenizing().sentTokenize(text)
    graph = build_graph(sentence_tokens)
    calculated_page_rank = nx.pagerank(graph, weight='weight')
    
    # most important sentences in ascending order of importance
    sentences = sorted(calculated_page_rank, key=calculated_page_rank.get, reverse=True)

    # return a 100 word summary
    summary = ' '.join(sentences)
    summary_words = summary.split()
    summary_words = summary_words[0:summary_length]
    dot_indices = [idx for idx, word in enumerate(summary_words) if word.find('।') != -1]
    #if clean_sentences and dot_indices:
    if  dot_indices:
        last_dot = max(dot_indices) + 1
        summary = ' '.join(summary_words[0:last_dot])
    else:
        summary = ' '.join(summary_words)
    return summary


"""
for i in range(1,151):
    i = str(i)
    f = open("Dataset/NCTB/Source/"+i+".txt","r")
    print("Input:")
    print(f.read())
    f2 = open("Dataset/NCTB/Summary/"+i+".txt","r")
    print("Human Made Summary:")
    print(f2.read())
    print("Our Machine Made Summary:")
    extract_summary("Dataset/NCTB/Source/"+i+".txt")

"""










