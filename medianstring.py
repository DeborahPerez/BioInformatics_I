import itertools


#l2='TTACCTTAAC GATATCTGTC ACGGCGTTCG CCCTAAAGAG CGTCAGAGGT'
#l2='GAGTAGGAGGCTGGCTAGCGCCATTGGGGAGGGTCTAGCGGT GTAGATTAACCGCAATGCTCGCAGCCGGACGAGGCTACTCTG AACATCTAGTACCGTACATCCAGAGAGGCGTATCAACAACCC GACCTTTGTCTTTGAAATCCGAGTTGGGAAGAGGCTTGAATT TTGGCTTCCAGTGAGGCTGCTGGCATCTGACTTCACCCTCGG CGGTTAGAGGCAGCATGGGCCCGCGCAGTTGACTTGAGTGAG TCGGACATTTGTGAGGCGCCTTGCATTTCAGCCCTTATCCCA GGCGATGTACAGAAAGCGGAGGCCCGAGGCGGCTCTATGAAG AGGACGAGCGCCGAGGCTCCTAACCGTACCTGGATAACCCAT GAGGCCAGGGATGCTTTACGTGACCGGCTGCGACTAGAGTCG'
l2='CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG'
kmer=7

def HammingDistance(g1, g2):
    distance = 0
    for i, j in zip(g1, g2):
        if i != j:
            distance = distance + 1
    return distance

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

def pattern2stringdst(dnastr,kmer):
    dna = list()
    dna[:]=[]
    for block in dnastr.split(' '):
        dna.append(block)
    totaldst=0

    for block in dna:
        hdst=99999999999
        chunksize=len(block) - len(kmer)
        for n in range(0, chunksize+1, 1):
            chunk=block[n:n+len(kmer)]
            currhdst=HammingDistance(kmer,chunk)
            if hdst>currhdst:
                hdst=currhdst
        totaldst=totaldst+hdst
    return totaldst

def medianstring(dna,klen):
    distance=99999999999
    median=''
    for n in range(0,4**klen,1):
        pattern=CumputeNumberToPatern(n,klen)
        tmpdst=pattern2stringdst(dna,pattern)
        if distance>tmpdst:
            distance=tmpdst
            median=pattern

    return median

def createallpaterns(l):
    resultado=list()
    for n in range(0, 4 ** l, 1):
        pattern = CumputeNumberToPatern(n, l)
        resultado.append(pattern)

    return resultado


print (medianstring(l2,6))
print ("-------------------")


outlst1=createallpaterns(10)

ls=itertools.product('ACGT',repeat=10)
outlst2=list()
print("!")
for l in ls:
    str=''
    for n in range(0,len(l),1):
        str=str+l[n]
    outlst2.append(str)
print ("!!")

print(len(outlst1))
print(len(outlst2))