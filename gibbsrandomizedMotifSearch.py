#2016 Jorge Canelhas
import sys

lines = sys.stdin.read().splitlines()
mtrx=list()
for n,l in enumerate(lines):
    if n==0:
        l1=l
    else:
        mtrx.append(l)
#l1='8 5 100'








#mtrx=['CGCCCCTCTCGGGGGTGTTCAGTAACCGGCCA','GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG','TAGTACCGAGACCGAAAGAAGTATACAGGCGT','TAGATCAAGTTTCAGGTGCACGTCGGTGAACC','AATCCACCAGCTCCACGTGCAATGTTGGCCTA']

size,nstrings,numberofiterations=l1.split(' ')
size=int(size)
nstrings=int(nstrings)
numberofiterations=int(numberofiterations)
#mtrx=['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA','GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG','TAGTACCGAGACCGAAAGAAGTATACAGGCGT','TAGATCAAGTTTCAGGTGCACGTCGGTGAACC','AATCCACCAGCTCCACGTGCAATGTTGGCCTA']
#mtrx=['GCAGTGACTTGTGCCCTGCGTCATAGTGGTTTAGACCGAAACGGGAGGGTTCCCCGAAGTAAGTTATGAGGGTGCAGTTGAAGCGTGAGATGCGAAAAAGTGACCTCGTTCCAGACTGCTGTCTAGCTTGATGTCCCGCGTTAAAAAACATTGCAGCGGATACGTTTGCGTGCAGTGACTTGTGCC','CTGCGTCATAGTGGTTTAGACCGAAACGGGAGGGTTCCCCGAAGTAAGTTATGAGGGTGCAGTTGAAGCGTGAGATGCGAAAAAGTGACCTCGTTCCAGACTGCTGTGGGCGGGACGTCGTACTAGCTTGATGTCCCGCGTTAAAAAACATTGCAGCGGATACGTTTGCGTGCAGTGACTTGTGCC','GCCCACTTGTGCGCTTGCCTGACCATAATCCTTGGGACACTTACTCAGGGATGCCGTACACGGGAGCGTAGACTACCCAATTACGGTTTACGTCTAGGACGACTAAGGGTCCCGCGTCGTACGGTTCAGGAGGCTTGTTAGCGCAGCACCTGTGCTGCGAGGACGGCGATAGGTTAGGCAACAGTC','TCTGACCTGAGCCCTGGGATGGCGTTCGTCGGTCAGCCCCTGACGACCGAAACCTGACGCGTAAAATCACCGTAGGAGCGCTTGGCATTCCGACGTCTCGCTAAAGTATATTAATTGCCCGCCACTGGGTCTGACGAAATAGCTCTTATGGCGTTCTTCTCAATTGTTGCTTTCAGCATATCTAGC','TCAGTACGCTCAAAGGACTCGCAGTATATGGTACTCAAGTCGACATCTGCAGAAAATATACTCGAGCGACACAATATTCCAATTGTACGCTCAAGCGACATTGTCTCTCAGGTCGGCACCCTCCCGGAGATGGCTTACCCGTGTGGCAGACACTGACTATACTTGTCCGTCTGACGTCGTCAATTT','TTTATAGACTAAGTGTCACTACGTAATGAAGCAAGTTCTCTGCCTCCACGTTTATAAGCATAGTGCACCACCACCTCCTATGGGGTCTGACGTCTCTGCATCAGATCGGCCGGCGATGACCAGGTTCATGGTACTCTGCCTCGGTGACGCAATTGCATACCCGTACAGTCACTGCAAGATACGAAA','AAATTCGCCTCAATTATTGCGGCGAGTTCACTAACCTCGCGAGACAGACTTTAGATAGCTAACATCTGAAACGTTCTGTCCCACTGTAAGTGTGGGTCTGCTTTCGTAGCCAAGTGATATGTTCGGGCGGCAGAATATCTAAGGGAACACATCGACAGTTCCAGGCAGCGTCCAGACCTCAGCCGC','GGTGGTTGGTGGTTGTCGATAACCCACTGTAAGGGCGTTTGGCAAAAAGTCTAGCGTTATCCACGCGAAGTGCCCTGATGGGAGTACACCCGTTTCCATTGAGAAAACCACGTGGATCGCGCAACTGACGTCGTACGACCGTATCACTCGAGCTATCCGCTCCTAGTTCTGGAGGATGGAAACTTC','CTCAAAGCATCGCCAGCGCAAGCCCTTGTAGCCCCGGAGGCGCAGATATGGCCGAGAGGAACTATTGGGTCTGATCACGTATTCAGTCCTTAGAAGAAATGTTCTGTAAAGCGCGTACATGTGACAGTCCTGTCGGACCAGGCGCCGCTCCAAACGAACGTGCTTCAAATTCACTAGACCTAAAAT','AGTTCAAGCAAATGAATGAGGAGGATGCTATTGAGAATCAATACTCACATGTTGCAACACGTGGGGAGTTGAGTTATCGGGAAACGATCTACGCTCCATATCCGTACGGGACGCCTACGTCCGCAAGGGCACGTCACAAGCCATAGAAGGGTTGTACGTCGTAAACTGCTCGACAACTCGGTAGCG','ACCGAGGCTTACTGCGGACTTGACCAAAAAGCAGGGGGTCCCGCGTCGTATTATAGACGTCAGTCGAAAGCGCCTGAAAGACCGGATGCAAGTTCAATATGTTAGTCAGTTGACAACCTTCGGTGTCGTGTCAACTCGGGCTAAAGCTGTAAGTTGAGCAGATGCAGACTGATACCCAGAGGTGTG','TCATGCACGAGCAAAGTGATTCGTTTACTGCCGACTTTCTGATAGGTAAATCATGAGAATAGGGAGTGTCCAAAAGGCGGTTCACTCCGGAGAAGCGAGCATTAAGACGTTGCCTCGGCTTCCACTTAGCAACGATACTCTTGGGATGCAGGGGCTTGGAGGATGCTTTCTGACGTCGTACTTAGT','CTCTTATTGAGAGTTGAGCCTACAGATACCAAGGCTGGATGTTCGCAAGGGTTCGAATAGACGCACCTTGATGGAACCAACATTGTGCATTCCTTGCTGTTGTAACTATCTGGGTCTCGTGTCGTACCCCTAATCGTAAGGCGTAGGCGAGTAGGGGAAAAGTTCCCGTCTATGAGTCATTCCAGA','TTGCTTAGTGGAATCGACAGGACGTCGTAATAGAAAAGCTCCCACACTATCTGTATCCCTCTAACCGCTTTAATCCAGACATCCAGATCGGGCATGCCCGTCCCATATAGCGGAATCATATATTAGCTGGGCCGCCGTCCCACGGAATGTTCTGCTTTTGTTCCGAAATTGGAATTGACGTCGTAC','CCCTACAGTTTCCGCTAGCGGTTTATAGATTCAGGACGACCCGAAAGATCTGTACCAACGTGCGCATGTCTAAACATAATGGGAGGAAGTTTCAGCGGCCCGCGAAACGTAGGTGATCACTAATTCCGCCTGCATGACAGTCACGGACGCTCGTGACTCAGGGTCTACGGTCGTAACGTGGGATGT','TGTGATAATCTGTGGGTAACACGTCGTAATCGGATAGGATAAGACGAGACACTTTAAGTTCTGCGCGTCCTGTGGGTCCCGCGTGCGTCTGCACTAGCCCTCCATGCTCTATATCTCCTATATAAGCACGGACGCCACAGACCCCTCATTGAGCCTAGTAGGAGTCGTCGACCACGCTCCGGTAAC','CTCGGTAGAGGGTAGCAGTGACGTGACTACGTGCTCTACTGAAGATCCACCAAGTATGGTCTGACGTCGCCTCTGCTGTGGCCCATCGCCAGTGGGGTGGGCATAAGTCCTGCTACGTCTACTATCGGTTCTGTATGTCTGAATAGCCGGGAACGCCGATTCCAGCAGCGCGGAGCAGTAGAGGAC','ATTCTATCGTCTGGCCCATGATCTTGCATCGTTTTGGTAGGAAGTTCTGCTTCGCGGTGTCACCAATCACCGGACGAGGGTCTCTGCTTGTTCTTGGGCGAGACGTCGTAAGGACTACGTACGAGAAGGCATTCTACCTTCACTCGGGGCGAGTCATCGTAGGCTTCCACTTCATGTCGTCTGGTA','CCGGGGAAGCTCACTTAACACCAGTACTAGGGGGGTCTGACGTAACAGAGTCCCGAAAGTTTCGGTTCCCGTCACTGCGCGAGCGTTCCATTGCTTATGCTTTACCTACGGATGTGTCCCCACATGTAGGCGTCGTTACGTTTGACGGCCTCCACGTCGGCACTATAAAGGTTCTTAGCCGAACCA','GTTAGGAAGCGCCGTCTATGTGTTGGGGTCTGACTGAGTAGGACTGCAATCTGACTCCTTGGAGCTGACGACTGAAATTTCGCTATATATCTCCCTTCTTTAGGCTGGATGGGATAAAAGCGAATCCATGCTCCCCGCTCAGCAGGCCGCTTTGGAGTACTGTTTTGTTGTGCGCTAAAGTCCGAG']

import math
import random
import copy

def profile_pseudocount(mtrx):
    columns=[''.join(str) for str in zip(*mtrx)]
    #count=  [[col.count(nuc) for nuc in 'ACGT'] for col in columns]
    profile=list()
    profile[:]=[]
    for col in columns:
        tmpprof=list()
        tmpprof[:]=[]
        for nuc in 'ACGT':
            nnuc=float(col.count(nuc))+1.0
            lencol=float(len(col))+4 #como adicionamos 1 a cada base, temos de adicionar 4 ao denominador
            tmpprof.append(nnuc / lencol)
        profile.append(tmpprof)
    #profile=  [[float(col.count(nuc)) / float(len(col)+4) for nuc in 'ACGT'] for col in columns]

    return (profile)

def profileprobkmer(dna,size,mtrx):
    mostprobable=''
    maxprob=0
    chunksize = len(dna) - size
    for n in range(0, chunksize + 1, 1):
        prob = 1.0
        chunk = dna[n:n + size]
        for n,nuc in enumerate(chunk):
            if nuc=='A':
                prob=prob*(mtrx[n][0])
            elif nuc == 'C':
                prob = prob * ( mtrx[n][1])
            elif nuc == 'G':
                prob = prob * ( mtrx[n][2])
            else  :
                prob = prob * ( mtrx[n][3])
        if maxprob<prob:
            maxprob = prob
            mostprobable=chunk

    return  mostprobable
def score(motifs):
    #
    columns = [''.join(seq) for seq in zip(*motifs)]
    mx_count = sum([max([c.count(nuc) for nuc in 'ACGT']) for c in columns])
    return len(motifs[0])*len(motifs) - mx_count

def randomizedmotifsearchGibbs(Dna,k,t):
#    print('----')
    strlen=len(Dna[0])
    bestmotifs=list()
    motifs=list()
    optoutmotif=random.randint(0,t)
    for i in range(0,t):
        if optoutmotif!=i:
            rndstartpos=(random.randint(0,strlen-k))
            motifs.append(Dna[i][rndstartpos:rndstartpos+k])

    bestmotifs=copy.copy(motifs)

    while True:
        profile=profile_pseudocount(motifs)
        motifs[:]=[]
        for n,i in enumerate(mtrx):
            pkmer=profileprobkmer(Dna[n],k,profile)
            motifs.append(pkmer)
        if score(motifs)<score(bestmotifs):
            bestmotifs = copy.copy(motifs)
        else:
            return bestmotifs
        #print(bestmotifs)
    return bestmotifs

supermotifs=list()
x=list()
x=randomizedmotifsearchGibbs(mtrx,size,nstrings)
supermotifs=copy.copy(x)
for i in range(1,numberofiterations):
    x[:]=[]
    x=randomizedmotifsearchGibbs(mtrx,size,nstrings)

    if score(x) < score(supermotifs):
        supermotifs=copy.copy(x)

        print(score(x))
    print (supermotifs)
for i in supermotifs:
    print(i)

#prof=profile_pseudocount(mtrx)
#print(prof)