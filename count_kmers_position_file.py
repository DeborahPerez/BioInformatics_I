#2016 Jorge Canelhas
f=open('dataset_3_5.txt','r')
l1=f.readline().strip()
l2=f.readline().strip()
count=0
print (l1)
print (l2)



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