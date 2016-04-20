#2016 Jorge Canelhas

import sys

#lines = sys.stdin.read().splitlines()
#chunk=lines[0] #string
#gene=lines[1] #gene
#l3=lines[2] #allowedmissmatches

chunk='AA'
gene='TACGCATTACAAAGCACA'
l3=1


def HammingDistance(g1, g2):
    distance=0
    for i,j in zip(g1,g2):
        if i!=j:
            distance=distance+1
    return distance


def approximatepatterncount(text,pattern,d):
    outlst=list()
    for i in range(0,len(gene)-len(chunk)+1):
        word=gene[i:i+len(chunk)]
        if HammingDistance(word,chunk)<=int(d):
            outlst.append(i)
    return len(outlst)

#for i in outlst:
   # print (i,end=" ")
#print()
print (approximatepatterncount(gene,chunk,l3))