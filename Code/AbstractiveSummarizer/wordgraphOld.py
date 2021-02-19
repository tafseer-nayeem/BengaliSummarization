import nltk
import takahe2
import posTagger
sentences = []
        
def listToString(s):  
    str1 = " "      
    return (str1.join(s)) 

def summary(sentences):
    compresser = takahe2.word_graph(sentences, nb_words = 13, lang = 'bangla', punct_tag = "PUNCT" )

    # Get the 50 best paths
    candidates = compresser.get_compression(50)
    
    # 1. Rerank compressions by path length (Filippova's method)
    for cummulative_score, path in candidates:

        #normalize path score by path length
        normalized_score = cummulative_score / len(path)
        
    # Write the word graph in the dot format
    compresser.write_dot('test2.dot')

    # 2. Rerank compressions by keyphrases (Boudin and Morin's method)
    reranker = takahe2.keyphrase_reranker( sentences,  candidates, lang = 'bangla' )
    reranked_candidates = reranker.rerank_nbest_compressions()

    pathList = []
    # Loop over the best reranked candidates
    for score, path in reranked_candidates:

        #print the best reranked candidates
        print(round(score, 3), ' '.join([u[0] for u in path]))

        paths = ' '.join([u[0] for u in path])
        pathList.append(paths)
    
    return pathList


    
def takeinput(doc):
    del sentences[:]
    document = open(doc).read()
    print('document: ',document)
    documentList = list(document)
    
    dtext = ""
    l = 0
    
    for letter in documentList:    
        if ord(letter)== 2404:
            documentList[l] = '.'
        l = l +1
    WithFullstop = dtext.join(documentList)
    
    text = nltk.word_tokenize(WithFullstop)
    n = []
    for i in text:
        a=posTagger.pos()
        n.append(a.posTagging(i))
    n2= [list(l) for l in n]

    for i in range(len(n2)):
        if len(n2[i][0]) == 1:
            if (ord(n2[i][0]) == 46 or ord(n2[i][0]) == 44 or ord(n2[i][0]) == 33 or ord(n2[i][0]) == 63):
                n2[i][1] = 'PUNCT'
    n= [tuple(l) for l in n2]
    
    st =""
    for i in range(len(n)):
        st += n[i][0]+'/'+n[i][1]+' '
    sentence = st.split('./PUNCT ')
    
    
    for i in sentence:
        sentences.append(i+"./PUNCT")
        
    sentences.pop()    

    pathList = summary(sentences)

    if pathList:
        return pathList[len(pathList)-1]
    else: 
        return



