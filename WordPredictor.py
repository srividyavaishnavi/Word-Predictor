from collections import OrderedDict
import re

class WordPredictor():
 
    def __init__(self, filename):
        self.filename = filename
        self.bigram=self.wordpairFrequency()
 

    def get_most_likely_successor(self,curr):
        sbigram=self.bigram
        maxVal,flag=0,0
        x=""
        for (k,v) in sbigram.items():
            if k.startswith(curr):
                if v>maxVal:
                    x,maxVal=k.replace(curr,'').replace('_',''),v
                if flag==0:flag=1
            else:
                if flag==1:break
        return x
    
    def wordpairFrequency(self):
        with open(self.filename, 'r') as readfile:
            text=re.sub("[^\w+ ]+","",readfile.read().replace('\n',' ')) 
        bigrams={}
        lst=text.split()
        l=len(lst)
        for i in range(l-1):
            temp = lst[i]+"_"+lst[i+1]
            if not temp in bigrams:
                bigrams[temp] = 1
            else:bigrams[temp] += 1
        with open('l.txt','w') as r:r.write(str(dict(sorted(bigrams.items()))))
        return OrderedDict(sorted(bigrams.items()))
 
def test():
    wp = WordPredictor("11-0.txt")
    test_cases = [("Alice","was"),("was","a"), ("at","the")]
    for curr, next in test_cases:
        result = wp.get_most_likely_successor(str(curr))
        assert result==next, (curr, next,result)
        print("Success")



test()

