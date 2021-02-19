from BLTK.wordConverter import word as word_tokenize

serialList = []
serialList2 = []
for i in range(1,101):
    serialList.append(i)
    serialList2.append(i)

RemoveItem = [77]  
RemoveItem2 = [83]
serialList = [ele for ele in serialList if ele not in RemoveItem]
serialList2 = [ele for ele in serialList2 if ele not in RemoveItem2]

def getsummary(a,n):
    a = str(a)
    n = str(n)
    fmachine = open("Dataset/BNLPC/Dataset"+n+"/MachineGeneratedSummary/"+a+".txt","r").read()
    return fmachine

def getreference(a,n):        
    a = str(a)
    n = str(n)
    fmachine = open("Dataset/BNLPC/Dataset"+n+"/Summaries/Document_"+a+"_Summary_1.txt","r").read()
    return fmachine

def getsource(a,n):
    a = str(a)
    n = str(n)
    fmachine = open("Dataset/BNLPC/Dataset"+n+"/NormaliseDocument/Document_"+a+".txt","r").read()
    return fmachine

# -------------------------------------------------------------
#   MAIN FUNCTION
# -------------------------------------------------------------

if __name__=='__main__':
    
    CR_dict = {}
    CR_dict2 = {}
    sumCRScore = 0
    
    #Dataset1
    for i in serialList:
        summary = getsummary(i,1)
        references = getreference(i,1)
        source = getsource(i,1)

        s_tokenize = word_tokenize().sentToWord(source)
        h_tokenize = word_tokenize().sentToWord(references)

        s_set = set(s_tokenize)
        h_set = set(h_tokenize)

        commonTokLength = len(s_set.intersection(h_set))
        copyRate = float(commonTokLength) / float(len(h_set))

        CR_dict[i] = copyRate

    for k, v in CR_dict.items():
        print("SentenceID : {0}, CR Score : {1}".format(k, v))
        sumCRScore = sumCRScore + v
        
        
    #Dataset2
    for i in serialList2:
        summary = getsummary(i,2)
        references = getreference(i,2)
        source = getsource(i,2)

        s_tokenize = word_tokenize().sentToWord(source)
        h_tokenize = word_tokenize().sentToWord(references)

        s_set = set(s_tokenize)
        h_set = set(h_tokenize)

        commonTokLength = len(s_set.intersection(h_set))
        copyRate = float(commonTokLength) / float(len(h_set))

        CR_dict2[i] = copyRate

    for k, v in CR_dict2.items():
        print("SentenceID : {0}, CR Score : {1}".format(k, v))
        sumCRScore = sumCRScore + v

    print (sumCRScore)
    print (sumCRScore / (len(CR_dict)+len(CR_dict2)))
    
  
