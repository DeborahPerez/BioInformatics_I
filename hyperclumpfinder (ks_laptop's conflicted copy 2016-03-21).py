import sys
import copy




#lines = sys.stdin.read().splitlines()
#l1=lines[0]
#l2=lines[1]
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

        print (i)
        print(clumplist[i])


    print("Done")
    return clumplist



l1='CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA'
l2='5 50 4'
p1,p2,p3= l2.split(' ')
zed= (superclumpfinder(l1,int(p1),int(p2),int(p3)))

nkmers=0
for i in zed:
    if zed[str(i)]==-1:
        nkmers=nkmers+1
        print (i ,end=" ")
#print (nkmers)




