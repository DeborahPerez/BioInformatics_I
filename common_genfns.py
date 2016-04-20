#Library of common functions for bio informatics 1
#Jorge Canelhas jorge(dot)canelhas(at)binarium(dot)pt
#You are free to use and modify, don't forget to credit previous authors


def count_kmers(code,kmer):
    count=0
    codelen=len(code)+1
    kmerlen=len(kmer)
    for n in range(0,codelen-kmerlen,1):
        currpart=code[n:n+len(kmer)]
        if currpart==kmer:
            count=count+1
    return count

def locate_kmers(code,kmer):
    positions=list()
    codelen=len(code)+1
    kmerlen=len(kmer)
    for n in range(0,codelen-kmerlen,1):
        currpart=code[n:n+len(kmer)]
        if currpart==kmer:
            positions.append(n)
    return positions

def HammingDistance(g1, g2):
    distance=0
    for i,j in zip(g1,g2):
        if i!=j:
            distance=distance+1
    return distance

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
    out=''
    start=len(tmp)-1
    for i in range(start+1,0,-1):

        out=out+l2[i-1:i]
    return out

def wordfrequency(gene,size):
    mxcount=0
    counter=dict()
    result=list()
    codelen=len(gene)+1
    for n in range(0,codelen-size,1):
        kmer=gene[n:n+size]
        if counter.get(kmer, 0)==0:
            counter[kmer]=count_kmers(gene,kmer)
    return counter

def fastwordfrequency(text,k):
    frequentpaterns=list()
    frequencyarray=computingfrequencies(text,k)
    maxcount=max(frequencyarray)
    for i in range(0,4**k,1):
        if frequencyarray[i]==maxcount:
            pattern=CumputeNumberToPatern(i,k)
            frequentpaterns.append(pattern)
    return frequentpaterns

def CumputePatternToNumber(pattern):
    dic={'A':0,'C':1,'G':2,'T':3}
    total=0
    for n,i in enumerate(pattern):
        l=len(pattern)-n
        total=total+(dic[i]*(4**(l-1)))
    return total

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

def clumpfinder(gene,clumpsize,windowsize,minscore):
    result=dict()
    order=0
    codelen=len(gene)+1
    for n in range(0,codelen-windowsize,1):
        partition=gene[n:n+windowsize]
        tmp=wordfrequency(partition,clumpsize)
        for m in tmp:
            if tmp[m]>=minscore:
                if result.get(m, 0)==0:
                    result[m]=order
                    order=order+1
    parsedresult=list()
    for n in range(0,len(result)):
        parsedresult.append('0')
    for n in result:
        parsedresult[result[n]-1]=str(n)
    parsedresult.sort()
    return parsedresult

def fastclumpfinder(gene,clumpsize,windowsize,minscore):
    result=dict()
    order=0
    codelen=len(gene)+1
    for n in range(0,codelen-windowsize,1):
        partition=gene[n:n+windowsize]
        tmp=fastwordfrequency(partition,clumpsize)
        for m in tmp:
            #if tmp[m]>=minscore:
            if result.get(m, 0)==0:
                result[m]=1
            else:
                result[m]=result[m]+1
    parsedresult=list()
    for n in range(0,len(result)):
        parsedresult.append('0')
    for n in result:
        parsedresult[result[n]-1]=str(n)
    parsedresult.sort()
    return parsedresult


def superclumpfinder(gene,clumpsize,windowsize,minscore):
    mxcount=0
    counter=dict()
    positions=dict()
    result=dict()

    codelen=len(gene)+1
    for n in range(0,codelen-clumpsize,1):
        kmer=gene[n:n+clumpsize]
        if positions.get(kmer, 0)==0:
            #counter[kmer]=count_kmers(gene,kmer)
            positions[kmer]=locate_kmers(gene,kmer)

    for n in positions:
        if len(positions[n])>=minscore:
            insidewindow=False
            for i in range(0,len(positions[n])-1):
                if positions[n][i+1]-positions[n][i]<=50:
                    insidewindow=True

            if insidewindow==True:
                result[n]=[len(positions[n]),positions[n]]

    return result

def computingfrequencies(text,k):
    frequencyarray=list()
    for i in range(0,4**k,1):
        frequencyarray.append(0)
    for i in range(0,len(text)-(k-1)):
        pattern=text[i:i+k]
        j=CumputePatternToNumber(pattern)
        frequencyarray[j]=frequencyarray[j]+1
    return frequencyarray


def HammingDistance(g1, g2):
    for i,j in g1,g2:
        if i!=j:
            distance=distance+1
    return distance

