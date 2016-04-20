#2016 Jorge Canelhas
import sys

lines = sys.stdin.read().splitlines()
l1=lines[0]
l2=int(lines[1])

def computingfrequencies(text,k):
    frequencyarray=list()
    for i in range(0,4**k,1):
        frequencyarray.append(0)
    for i in range(0,len(text)-(k-1)):
        pattern=text[i:i+k]
        j=CumputePatternToNumber(pattern)
        frequencyarray[j]=frequencyarray[j]+1
    return frequencyarray

def CumputePatternToNumber(pattern):
    dic={'A':0,'C':1,'G':2,'T':3}
    total=0
    for n,i in enumerate(pattern):
        l=len(pattern)-n
        total=total+(dic[i]*(4**(l-1)))
    return total

for i in computingfrequencies(l1,l2):
    print(i,end=" ")