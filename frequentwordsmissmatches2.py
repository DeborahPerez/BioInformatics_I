import sys
import itertools

#lines = sys.stdin.read().splitlines()
#l1=lines[0]
#l2=lines[1]
#l1='CACAGTAGGCGCCGGCACACACAGCCCCGGGCCCCGGGCCGCCCCGGGCCGGCGGCCGCCGGCGCCGGCACACCGGCACAGCCGTACCGGCACAGTAGTACCGGCCGGCCGGCACACCGGCACACCGGGTACACACCGGGGCGCACACACAGGCGGGCGCCGGGCCCCGGGCCGTACCGGGCCGCCGGCGGCCCACAGGCGCCGGCACAGTACCGGCACACACAGTAGCCCACACACAGGCGGGCGGTAGCCGGCGCACACACACACAGTAGGCGCACAGCCGCCCACACACACCGGCCGGCCGGCACAGGCGGGCGGGCGCACACACACCGGCACAGTAGTAGGCGGCCGGCGCACAGCC'
#l2='10 2'
l1='ACGTTGCATGTCGCATGATGCATGAGAGCT'
l2='4 1'
#l1='CCAAGACTTGCGAGTTGCTCTAAGACTCTAGAGAGACAGACTTGCTTGCAGACTCTATCTATCTAAGACGAGGAGCCAAGACGAGTCTAAGACTCTAAGACGAGGAGTCTAGAGGAGAGACGAGAGACCCATTGCTCTAGAGAGACCCATTGCTCTAGAGTTGCTCTATCTACCACCATCTAGAGTTGCTTGCGAGTTGCTTGCGAGGAGCCAAGACAGACTCTAAGACGAGTTGCCCACCATCTATTGCGAGTCTATCTAAGACCCACCAGAGTTGCCCATCTACCAGAGGAGTTGCTCTAAGACTCTATTGCCCA'
#l2='7 3'
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


def frequentwords(code,size,acceptederror):
    mxcount=0
    result=list()
    kmerlst=dict()
    tmplst=dict()

    codelen=len(code)+1
    for n in range(0,codelen-size,1):
        kmer=code[n:n+size]
        tmplst=neighbours(kmer,acceptederror)
        for f in tmplst:
            if kmerlst.get(f, 0) == 0:
                kmerlst[f] = count_kmers(code, f) #nao vale a pena por mais....
                if mxcount<kmerlst[f]:
                    mxcount=kmerlst[f]

    for f in kmerlst:
        if kmerlst[f]==mxcount:
            result.append(f)

    return result
size,error=l2.split(" ")
outp=frequentwords(l1, int(size),int(error))
for i in outp:
    print (i ,end=" ")