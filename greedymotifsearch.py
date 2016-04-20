
l1='3 5'
kmersize,nstrings=l1.split(' ')
kmersize=int(kmersize)
nstrings=int(nstrings)

dna=['GGCGTTCAGGCA','AAGAATCAGTCA','CAAGGAGTTCGC','CACGTCAATCAC','CAATAATATTCG']


def profileprobkmer(dna,size,mtrx):

    mostprobable=''
    maxprob=0

    chunksize = len(dna) - size
    for n in range(0, chunksize + 1, 1):
        prob = 1.0
        chunk = dna[n:n + size]
        for n,nuc in enumerate(chunk):
            if nuc=='A':
                prob=prob*(mtrx[0][n])
            elif nuc == 'C':
                prob = prob * ( mtrx[1][n])
            elif nuc == 'G':
                prob = prob * ( mtrx[2][n])
            else  :
                prob = prob * ( mtrx[3][n])
        if maxprob<prob:
            maxprob = prob
            mostprobable=chunk

    return  mostprobable


def greedymotifsearch(dna,kmersize,nstrings):
    bestmotifs=list()
    for i in dna:
        bestmotifs.append(i[0:kmersize])






    return  bestmotifs


def score():


print(greedymotifsearch(dna,kmersize,nstrings))