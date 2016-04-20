import sys
#2016 Jorge Canelhas
#lines #2016 Jorge Canelhas= sys.stdin.read().splitlines()
#chunk=lines[0] #string
#gene=lines[1] #gene
#l3=lines[2] #allowedmissmatches

chunk='TGCT'
variation=1

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

#for i in outlst:
   # print (i,end=" ")
#print()
k=neighbours(chunk,variation)
for i in k:
    print (i,end='\n')

print (len(k))