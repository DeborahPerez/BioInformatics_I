
import sys

lines = sys.stdin.read().splitlines()
mtrx=list()
for n,l in enumerate(lines):
    if n==0:
        l1=l
    else:
        mtrx.append(l)
l2=''
for n in mtrx:
    l2=l2+ ' ' + n
l2=l2[1:len(l2)]




def HammingDistance(g1, g2):
    distance = 0
    for i, j in zip(g1, g2):
        if i != j:
            distance = distance + 1
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

def pattern2stringdst(dnastr,kmer):
    dna = list()
    dna[:]=[]
    for block in dnastr.split(' '):
        dna.append(block)
    totaldst=0

    for block in dna:
        hdst=99999999999
        chunksize=len(block) - len(kmer)
        for n in range(0, chunksize+1, 1):
            chunk=block[n:n+len(kmer)]
            currhdst=HammingDistance(kmer,chunk)
            if hdst>currhdst:
                hdst=currhdst
        totaldst=totaldst+hdst
    return totaldst

def medianstring(dna,klen):
    distance=99999999999
    median=''
    for n in range(0,4**klen,1):
        pattern=CumputeNumberToPatern(n,klen)
        tmpdst=pattern2stringdst(dna,pattern)
        if distance>tmpdst:
            distance=tmpdst
            median=pattern
    return median

def createallpaterns(l):
    resultado=list()
    for n in range(0, 4 ** l, 1):
        pattern = CumputeNumberToPatern(n, l)
        resultado.append(pattern)

    return resultado


kmerlen=int(l1)

print (medianstring(l2,kmerlen))