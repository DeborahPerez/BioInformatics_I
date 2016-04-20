import sys

lines = sys.stdin.read().splitlines()
l1=lines[0]
l2=lines[1]
count=0




def count_kmers(code,kmer):
    count=0
    codelen=len(code)+1
    kmerlen=len(kmer)
    for n in range(0,codelen-kmerlen,1):
        currpart=code[n:n+len(kmer)]
        if currpart==kmer:
            count=count+1
    return count

def frequentwords(code,size):
    mxcount=0
    counter=dict()
    result=list()
    codelen=len(code)+1
    for n in range(0,codelen-size,1):
        kmer=code[n:n+size]
        if counter.get(kmer, 0)==0:
            counter[kmer]=count_kmers(code,kmer)
            if mxcount<counter[kmer]:
                result[:]=[]
                result.append(kmer)
                mxcount=counter[kmer]
            elif mxcount==counter[kmer]:
                result.append(kmer)

    return result

for i in frequentwords(l1, int(l2)):
    print (i) ,