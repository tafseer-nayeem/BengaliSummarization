# -*- coding: utf-8 -*-

"""
Here it takes a paasage/article then do some processing and finally gives spllit
the article/passage into sentences.Then joining all sentences gives a flexible list
of sentences.
"""
'''
import codecs
with codecs.open("S.txt",'r',encoding="utf-8") as myfile:
    text= myfile.read()'''
class sentTokenizing:
    def sentTokenize(self,gettingText):
        dataToReSize=[]
        data=[]
        cleanText=''
        for i in gettingText:
            if i=='।' or i=='!' or i=='?':
                cleanText+=i
                dataToReSize.append(''.join(cleanText))
                cleanText=''
            else:
                if i=='\n' or i=='\r' or i=='”' or i=='“' or i=='"':
                    continue
                else:
                    cleanText+=i
        #print (dataToReSize)
        for i in dataToReSize:
            withoutAheadSpace=''
            flag=1
            for j in i:
                if j==' ' and flag:
                    continue
                else:
                    flag=0
                    withoutAheadSpace+=j
            data.append(''.join(withoutAheadSpace))
        #print(data)
                
        return data
 
#a=sentTokenizing().sentTokenize(text)
#print(a)
        
#a = sentTokenizing().sentTokenize("মাতৃস্নেহের তুলনা নাই। কিন্তু অতিস্নেহ অনেক সময় অমঙ্গল আনয়ন করে। যে স্নেহের উত্তাপে সন্তানের পরিপুষ্টি, তাহারই আধিক্যে সে অসহায় হইয়া পড়ে। মাতৃস্নেহের মমতার প্রাবল্যে মানুষ আপনাকে হারাইয়া আসল শক্তির মর্যাদা বুঝিতে পারে না। নিয়ত মাতৃস্নেহের অন্তরালে অবস্থান করিয়া আত্মশক্তির সন্ধান সে পায় না - দুর্বল অসহায় পক্ষীশাবকের মতো চিরদিন স্নেহাতিশয্যে আপনাকে সে একান্ত নির্ভরশীল মনে করে। ক্রমে জননীর পরম সম্পদ সন্তান অলস, ভীরু, দুর্বল ও পরনির্ভরশীল হইয়া মনুষ্যত্ব বিকাশের পথ হইতে দূরে সরিয়া যায়। অন্ধ মাতৃস্নেহ সে কথা বুঝে না অলসকে সে প্রাণপাত করিয়া সেবা করে ভীরুতার দুর্দশা কল্পনা করিয়া বিপদের আক্রমণ হইতে ভীরুকে রক্ষা করিতে ব্যস্ত হয়।")
#print(a)
