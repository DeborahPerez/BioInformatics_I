#2016 Jorge Canelhas

import sys

lines = sys.stdin.read().splitlines()
chunk=lines[0] #string
gene=lines[1] #gene
l3=lines[2] #allowedmissmatches

#chunk='CTGATCC'
#gene='GATCGAATTGGCTTGCGCCCACATCCACCTCCCACTACCGCATCACTGGACGGGCCTAATGCCACGCCAACCAGTACGCTTTCCGGCTGATCCCGACTATAATTGTCAACCCTCGTGATTCGGTTCACGACGGTCATCGGACGGTACGGTGTCCGACCCACCGCGTTAGCGGTAGGATAGGCTCTGAATGCAGGGCAAAATTCTAAACTGCTCGTAGGCAATGTGTCGTTCGGTGTTTCGTATGGTATGCTTTCCAAATAGCGAATCCAACAGGTTAACATCTGGGGGCACTGAGTGAAGCGGCCGATGCTT'
#l3=2


def HammingDistance(g1, g2):
    distance=0
    for i,j in zip(g1,g2):
        if i!=j:
            distance=distance+1
    return distance
outlst=list()


for i in range(0,len(gene)-len(chunk)+1):
    word=gene[i:i+len(chunk)]
    if HammingDistance(word,chunk)<=int(l3):
        outlst.append(i)


#for i in outlst:
   # print (i,end=" ")
#print()
print (len(outlst))