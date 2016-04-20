#2016 Jorge Canelhas

import sys
import itertools

#lines = sys.stdin.read().splitlines()
#l1=lines[0]
#l2=lines[1]
l1='TTATGTTTTTTTGTTATTTCATGTTTTGTTTCATTATTTTGTGTTACATTATTTTTTTGTTTTTTTTTTTTTTTTTTTTTCATTTTTTTTATGTTATTACATTTTTTCATTATTATTATTTTTTTTTTTTCATTATTTTGTTATTATTTTGCATTTTTATGTTTTTTTTACACATTATTATTTCATGTTTTTACATGTTACACATGCATTTTTTTTTTGCATTTTTATTTTGCATTTTTTCATTT'
l2='5 2'
#l1='ACGTTGCATGTCGCATGATGCATGAGAGCT'
#l2='4 1'

#l1='AAAAAAAAAA'
#l2='2 1'

count=0

def HammingDistance(g1, g2):
    distance=0
    for i,j in zip(g1,g2):
        if i!=j:
            distance=distance+1
    return distance

def count_kmers(code,kmer):
    count=0
    codelen=len(code)+1
    kmerlen=len(kmer)
    for n in range(0,codelen-kmerlen,1):
        currpart=code[n:n+len(kmer)]
        if currpart==kmer:
            count=count+1
    return count

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


def neighbours(chunk,vr):
    outlst=list()
    tmplst=list()
    lc=len(chunk)
    outlst[:] = []
    for n in range(0,4**lc,1):
        t=CumputeNumberToPatern(n,len(chunk))
        ds=HammingDistance(chunk,t)
        if ds<=vr:
            outlst.append(t)
    return outlst

def reverse_complement(gene):
    tmp=''
    for i in gene:
        if i=='A':
            tmp=tmp+'T'
        elif i=='T':
            tmp=tmp+'A'
        elif i=='G':
            tmp=tmp+'C'
        else:
            tmp=tmp+'G'

    return tmp

def frequentwords(code,size,acceptederror):
    mxcount=0
    counter=dict()
    result=list()
    tmplist=dict()
    codelen=len(code)+1
    for n in range(0,codelen-size,1):
        kmer=code[n:n+size]
        #tmplist[:]=[]
        tmplst = neighbours(kmer, acceptederror)
        if counter.get(kmer, 0)==0:
            counter[kmer] =0
            for tmpkmer in tmplst:
                revtmpkmer=reverse_complement(tmpkmer)
                nkmers=count_kmers(code,tmpkmer)+count_kmers(code,revtmpkmer)
                counter[kmer]=counter[kmer]+nkmers
            if mxcount<counter[kmer]:
                result[:]=[]
                result.append(kmer)
                result.append(revtmpkmer)
                mxcount=counter[kmer]
            elif mxcount==counter[kmer]:
                result.append(kmer)
                result.append(revtmpkmer)


    return result


size,error=l2.split(" ")
outp=frequentwords(l1, int(size),int(error))
for i in outp:
    print (i ,end=" ")