import sys
import copy

#lines = sys.stdin.read().splitlines()
#l1=lines[0]
#l2=lines[1]
count=0

#2016 Jorge Canelhas
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


def superclumpfinder(gene,clumpsize,windowsize,minscore):
    clumplist=dict()
    #finallist=dict()
    windowlist=list()
    for i in range(0,4**clumpsize):
        clumplist[CumputeNumberToPatern(i,clumpsize)]=0
        #finallist[CumputeNumberToPatern(i,clumpsize)]=0

    for i in range(0,len(gene)-windowsize+1,1):
        window=gene[i:i+windowsize]
        windowlist.append(window)


        #clumpcompleted=False
        for j in windowlist:
            for i in clumplist:
                if clumplist[str(i)]>=0:
                    clumplist[str(i)]=0

                    k=0
                    while k<len(j)-clumpsize+1:
                    #for k in range(0,len(j)-clumpsize+1,1):
                        chunk=j[k:k+clumpsize]
                        if str(i)==chunk:
                            if clumplist[i]>=0:
                                #print (clumplist.get(str(i), 0))
                                clumplist[str(i)]=clumplist[str(i)]+1
                                #k=k+clumpsize
                        if clumplist[str(i)]>=minscore:
                            clumplist[str(i)]=-1
                        k=k+1

    return clumplist


l1='ACGTACGT'
l2='1 5 2'
l1='AAAACGTCGAAAAA'
l2='2 4 2'
l1='CCACGCGGTGTACGCTGCAAAAAGCCTTGCTGAATCAAATAAGGTTCCAGCACATCCTCAATGGTTTCACGTTCTTCGCCAATGGCTGCCGCCAGGTTATCCAGACCTACAGGTCCACCAAAGAACTTATCGATTACCGCCAGCAACAATTTGCGGTCCATATAATCGAAACCTTCAGCATCGACATTCAACATATCCAGCG'
l2='3 25 3'
l1='CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA'
l2='5 50 4'
p1,p2,p3= l2.split(' ')
zed= (superclumpfinder(l1,int(p1),int(p2),int(p3)))

for i in zed:
    if zed[str(i)]==-1:
        print (i ,end=" ")




