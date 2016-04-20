

f=open('dataset_2_6.txt','r')
l1=f.readline().strip()
l2=f.readline().strip()
count=0
print (l1)
print (l2)



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