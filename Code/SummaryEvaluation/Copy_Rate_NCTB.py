from BLTK.wordConverter import word as word_tokenize

serialList = []
for i in range(1,140):
    serialList.append(i)

def getsummary(a):
    a = str(a)
    fmachine = open("Dataset/NCTB/MachineGeneratedSummary/"+a+".txt","r").read()
    return fmachine

def getreference(a):        
    a = str(a)
    fmachine = open("Dataset/NCTB/Summary/"+a+".txt","r").read()
    return fmachine

def getsource(a):
    a = str(a)
    fmachine = open("Dataset/NCTB/Source/"+a+".txt","r").read()
    return fmachine

# -------------------------------------------------------------
#   MAIN FUNCTION
# -------------------------------------------------------------

if __name__=='__main__':
    
    CR_dict = {}
    sumCRScore = 0
    
    for i in serialList:
        
        summary = getsummary(i)
        references = getreference(i)
        source = getsource(i)
        
        s_tokenize = word_tokenize().sentToWord(source)
        h_tokenize = word_tokenize().sentToWord(references)

        s_set = set(s_tokenize)
        h_set = set(h_tokenize)

        commonTokLength = len(s_set.intersection(h_set))


        copyRate = float(commonTokLength) / float(len(h_set))

        print (copyRate)

        CR_dict[i] = copyRate

    for k, v in CR_dict.items():
        print("SentenceID : {0}, CR Score : {1}".format(k, v))
        sumCRScore = sumCRScore + v

    print (sumCRScore)
    print (sumCRScore / len(CR_dict))
    
  
