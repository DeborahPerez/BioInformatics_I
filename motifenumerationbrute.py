#2016 Jorge Canelhas
import sys

#lines = sys.stdin.read().splitlines()
#l1=lines[0]
#l2=lines[1]
#l3=lines[2]
#l4=lines[3]
#l5=lines[4]

l1='3 0'
l2='ACGT'
l3='ACGT'
l4='ACGT'

l1='3 1'
l2='AAAAA'
l3='AAAAA'
l4='AAAAA'


#l2='TCGCGCTTCATTTTTTAGTTCCATA'
#l3='CCGCTCCTTAAAAACATGTTTTCGG'
#l4='GCGCCTCCCTCGGCGCGAGCACTTA'
#l5='ACGCGGGACGTCTCAGCGTGTGATG'
#l6='AAGTGTCTTGTCGCCTAATAAGCTA'
#l7='TACTACCTATACGCATGAACTCCGC'

ksize,mismatches=l1.split(' ')
ksize=int(ksize)
mismatches=int(mismatches)
mtrx=[l2,l3,l4]


def count_kmers(code,kmer):
    count=0
    codelen=len(code)+1
    kmerlen=len(kmer)
    for n in range(0,codelen-kmerlen,1):
        currpart=code[n:n+len(kmer)]
        if currpart==kmer:
            count=count+1
    return count

def HammingDistance(g1, g2):
    distance=0
    for i,j in zip(g1,g2):
        if i!=j:
            distance=distance+1
    return distance
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
    for n in range(0,4**lc,1):
        t=CumputeNumberToPatern(n,len(chunk))
        ds=HammingDistance(chunk,t)
        if ds<=vr:
            outlst.append(t)
    return outlst

def wordlist(mtx,size,mismatches):
    tmpresult=dict()
    result=list()


    for l in mtx:
        code=l
        codelen=len(code)+1
        for n in range(0,codelen-size,1):
            kmer=code[n:n+size]
            if tmpresult.get(kmer, 0)==0:
                tmpresult[kmer]=1

    for n in tmpresult:
        kmer=n
        result.append([kmer,neighbours(kmer,mismatches)])
    return result



#usar a primeira linha para apanhar todos os kmers possiveis

kmers=wordlist(mtrx,ksize,mismatches)

#print(kmers)
outlst=list()


for k in kmers:
    kcount=0
 #   print(k[0])
    for l in mtrx:
        for m in k[1]:
            if count_kmers(l,m)>0:
                kcount=kcount+1
    lm=len(mtrx)
    if kcount>=lm:
        outlst.append(k[0])

for i in outlst:
    print(i, end=' ')