import sys

lines = sys.stdin.read().splitlines()
l1=lines[0]
l2=lines[1]
count=0



def count_kmers_positions(code,kmer):
    out = ''
    codelen=len(code)+1
    kmerlen=len(kmer)
    for n in range(0,codelen-kmerlen,1):
        currpart=code[n:n+len(kmer)]
        if currpart==kmer:
            out=out+ str(n) + " "
    return out


print (count_kmers_positions(l2, l1))