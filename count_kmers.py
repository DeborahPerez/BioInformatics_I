
#2016 Jorge Canelhas
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


print (count_kmers(l1, l2))