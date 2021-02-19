
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
