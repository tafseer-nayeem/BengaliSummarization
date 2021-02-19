
#Get the length of the NCTB source, summary and machine generated summary
serialList = []
for i in range(1,140):
    serialList.append(i)

length = {}
sumlength = 0
    
for i in serialList:
    a = str(i)
    f1 = open('Dataset/NCTB/MachineGeneratedSummary/'+a+'.txt').read()
    
    datalist = f1.split(' ')
    
    length[i] = len(datalist)


for k, v in length.items():
    print("SentenceID : {0}, Length : {1}".format(k, v))
    sumlength = sumlength + v

print (sumlength)
print (sumlength / len(length))

"""
#Get the length of the BNLPC source, summary and machine generated summary
serialList = []
serialList2 = []
for i in range(1,101):
    serialList.append(i)
    serialList2.append(i)

RemoveItem = [77]  
RemoveItem2 = [83]
serialList = [ele for ele in serialList if ele not in RemoveItem]
serialList2 = [ele for ele in serialList2 if ele not in RemoveItem2]

length = {}
length2 = {}
sumlength = 0
 
for i in serialList:
    a = str(i)
    #f1 = open('Dataset/Dataset1/MachineGeneratedSummary/'+a+'.txt').read()
    #f1 = open('Dataset/Dataset1/NormaliseDocument/Document_'+a+'.txt').read()
    f1 = open('Dataset/Dataset1/Summaries/Document_'+a+'_Summary_1.txt').read()
    
    datalist = f1.split(' ')
    
    length[i] = len(datalist)
    #print(a) 

for k, v in length.items():
    print("SentenceID : {0}, Length : {1}".format(k, v))
    sumlength = sumlength + v

for i in serialList2:
    a = str(i)
    #f1 = open('Dataset/Dataset2/MachineGeneratedSummary/'+a+'.txt').read()
    #f1 = open('Dataset/Dataset2/NormaliseDocument/Document_'+a+'.txt').read()
    f1 = open('Dataset/Dataset2/Summaries/Document_'+a+'_Summary_1.txt').read()
    datalist = f1.split(' ')
    
    length2[i] = len(datalist)
    #print(a)
    
for k, v in length2.items():
    print("SentenceID : {0}, Length : {1}".format(k, v))
    sumlength = sumlength + v

print(len(length)+len(length2))
print (sumlength)
print (sumlength / (len(length)+len(length2)))

"""




