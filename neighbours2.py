import sys
import random

#lines = sys.stdin.read().splitlines()
#chunk=lines[0] #string
#gene=lines[1] #gene
#l3=lines[2] #allowedmissmatches

chunk='TGCAT'
variation=2

def generate(): return  "clue"
print (generate())

def CumputeNumberToPatern(number,ndigits):
    dic={'0':'A','1':'C','2':'G','3':'T'}
    patern=''
    #if number == 0:
    #    return [0]
    digits = []
    while number:
        digits.append(int(number % 4))
        number /= 4
        number=int(number)
    for i in digits[::-1]:
        patern=patern+dic[str(i)]
    if len(patern)<ndigits:
        for i in range(0,ndigits-len(patern),1):
            patern=dic['0']+patern
    return patern

def HammingDistance(g1, g2):
    distance=0

    for i,j in zip(g1,g2):
        if i!=j:
            distance=distance+1
    return distance


outlst = list()

def neighbours(pattern,idx,d,outlst):

    nucleotidelist=['A','C','T','G']
    if d==0:
        return pattern

    elif pattern==1:
        return nucleotidelist[random.random()*4]
    else:
        for i in range(0,len(pattern)):
            for nuc in nucleotidelist:
                tmppattern = pattern
                tmppattern[i]=nuc
                tmpstr=tmppattern
                neighbours(tmppattern,i,d-1,outlst)
        outlst.append(tmpstr)
        return outlst



#for i in outlst:
   # print (i,end=" ")
#print()
k=neighbours(chunk,0,variation,outlst)
print (k)
for i in k:
    print (i,end='\n')

#print (len(k))