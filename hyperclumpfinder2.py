import sys
import copy

#lines = sys.stdin.read().splitlines()
#l1=lines[0]
#l2=lines[1]


#f=open('E-coli.txt','r')
#l1=f.readline().strip()
#l2='9 500 3'

count=0


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

def locate_kmers(code,kmer):
    positions=list()
    codelen=len(code)+1
    kmerlen=len(kmer)
    for n in range(0,codelen-kmerlen,1):
        currpart=code[n:n+len(kmer)]
        if currpart==kmer:
            positions.append(n)
    return positions

def superclumpfinder(gene,clumpsize,windowsize,minscore):
    clumplist=dict()
    finaldict=dict()
    tmplist=list()
    for i in range(0,4**clumpsize):
        pattern=CumputeNumberToPatern(i,clumpsize)
        tmplist[:]=[]
        tmplist=locate_kmers(gene,pattern)

        if len(tmplist)>=minscore:
            clumplist[pattern]=copy.deepcopy(tmplist)


#    for i in range(0,len(gene)-windowsize+1,1):
#        window=gene[i:i+windowsize]
#        windowlist.append(window)

    for i in clumplist:
        dbg=len(clumplist[i])-minscore
        for k in range(0,len(clumplist[i])-minscore+1,1):
            tmplist[:]=[]
            tmplist=copy.deepcopy(clumplist[i])
            dbg=tmplist[k]
            dbg=tmplist[k+minscore-1]
            dbg=tmplist[k+minscore-1]-tmplist[k]
            if tmplist[k+minscore-1]-tmplist[k]<=windowsize-clumpsize:
                finaldict[str(i)]=clumplist[str(i)]


    return finaldict


#l1='ACGTACGT'
#l2='1 5 2'
#l1='AAAACGTCGAAAAA'
#l2='2 4 2'
l1='CCACGCGGTGTACGCTGCAAAAAGCCTTGCTGAATCAAATAAGGTTCCAGCACATCCTCAATGGTTTCACGTTCTTCGCCAATGGCTGCCGCCAGGTTATCCAGACCTACAGGTCCACCAAAGAACTTATCGATTACCGCCAGCAACAATTTGCGGTCCATATAATCGAAACCTTCAGCATCGACATTCAACATATCCAGCG'
l2='3 25 3'
#l1='CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA'
#l2='5 50 4'
p1,p2,p3= l2.split(' ')
zed= (superclumpfinder(l1,int(p1),int(p2),int(p3)))

nkmers=0
for i in zed:
    nkmers=nkmers+1
    print (i ,end=" ")
#print (nkmers)




