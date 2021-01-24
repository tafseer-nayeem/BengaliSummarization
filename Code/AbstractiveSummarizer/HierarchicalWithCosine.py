from __future__ import print_function
import collections
import nltk
import re
import matplotlib.pyplot as plt
from sklearn.manifold import MDS
from sklearn.metrics.pairwise import cosine_similarity
from scipy.cluster.hierarchy import ward, dendrogram
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as shc
from sklearn.metrics import silhouette_score

def tokenize_only(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Zঅ-ঔং ৎ  ক-‍ঁ ]', token):
            filtered_tokens.append(token)
    return filtered_tokens

def startF(document):
    stopword = open('stopwords-bn.txt').read().split('\n')
    n_clusters = tfidf(document,stopword)
    filenamee1, n  = peep(n_clusters)
    return filenamee1, n 

def tfidf(document,stopword):
    tfidf_vectorizer = TfidfVectorizer(max_df=10, min_df=2, use_idf=True, tokenizer=tokenize_only, ngram_range=(1,3))    
    tfidf_matrix = tfidf_vectorizer.fit_transform(document)       
    terms = tfidf_vectorizer.get_feature_names()
    n_clusters = similarityDistance(tfidf_matrix,document)
    return n_clusters 

def similarityDistance(tfidf_matrix,document):      
    similarity_distance = 1 - cosine_similarity(tfidf_matrix)
    n_clusters = multidimensionalScaling(similarity_distance,document)
    return n_clusters
    
def multidimensionalScaling(similarity_distance,document):
    mds = MDS(n_components=2, dissimilarity="precomputed", random_state=1)
    pos = mds.fit_transform(similarity_distance)  # shape (n_components, n_samples)
    xs, ys = pos[:, 0], pos[:, 1]
    n_clusters = hierarchicalClustering(similarity_distance,pos,document)
    return n_clusters

def hierarchicalClustering(data,pos,document):

    key = 0
    k = []
    my_dict = dict()
    silhouette_scores = [] 
    for n in range(2,len(document)):
        cluster1 = AgglomerativeClustering(n_clusters=n, affinity='euclidean', linkage='ward')
        y1 = cluster1.fit_predict(pos)
        
        #Calculate Silhouette Scores
        silhouette_scores.append( silhouette_score(pos, y1)) 
        k.append(n)
        my_dict[key]= n
        key = key + 1
    
    print(silhouette_scores)
    
    #Find the maximum Silhouette Score
    maxx = silhouette_scores.index(max(silhouette_scores))
    print(maxx)
    
    # Plotting a bar graph to compare the results 
    plt.bar(k, silhouette_scores) 
    plt.xlabel('Number of clusters', fontsize = 20) 
    plt.ylabel('S(i)', fontsize = 20) 
    plt.show()
    
    #Get the no of cluster which have maximum Silhouette Score    
    val = list(my_dict.values())
    n_clusters = val[maxx]
    
    #Find the agglomerativeClustering
    cluster1 = AgglomerativeClustering(n_clusters=n_clusters, affinity='euclidean', linkage='ward')
    y1 = cluster1.fit_predict(pos)
    
    #Create file    
    p = str(n_clusters)
    f = open("tmp/cluster"+p+".txt","w")
    f.truncate(0)
    f = open("tmp/cluster"+p+".txt","a+")
    
    #Save the clusters in the temporary file
    clusters = collections.defaultdict(list)
    for i, label in enumerate(cluster1.labels_):
        clusters[label].append(i)
    dict(clusters)
        
    for cluster in range(n_clusters):
        print("cluster ",cluster,":")
        for i,sentence in enumerate(clusters[cluster]):
            print("\tsentence ",i,": ",document[sentence])
            f.write(document[sentence])
            f.write(" ")
        f.write('\n\n')  
        
    return n_clusters 
    
def peep(n):    
    p = str(n)
    cluster_sentence1 = open("tmp/cluster"+p+".txt").read().split('\n\n')
    cluster_sentence1.pop((len(cluster_sentence1))-1)
    print("Cluster Sentences are:",cluster_sentence1)
    filenamee1 = []
    for j in range(n):
        ab = str(j)
        namee = "tmp/Cluster"+p+"."+ab+".txt"
        filenamee1.append(namee)
        with open(namee, 'w') as f:
            for item in cluster_sentence1[j]:
                f.write(item)
    return filenamee1, n 
                








