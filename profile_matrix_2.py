mtrx=['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA','GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG','TAGTACCGAGACCGAAAGAAGTATACAGGCGT','TAGATCAAGTTTCAGGTGCACGTCGGTGAACC','AATCCACCAGCTCCACGTGCAATGTTGGCCTA']
mtrx=['TCGGGGGTTTTT','CCGGTGACTTAC','ACGGGGATTTTC','TTGGGGACTTTT','AAGGGGACTTCC','TTGGGGACTTCC','TCGGGGATTCAT','TCGGGGATTCCT','TAGGGGAACTAC','TCGGGTATAACC']



import math



def profile(mtrx):
    columns=[''.join(str) for str in zip(*mtrx)]
    count=  [[col.count(nuc) for nuc in 'ACGT'] for col in columns]
    profile=list()
    profile[:]=[]
    for col in columns:
        tmpprof=list()
        tmpprof[:]=[]
        for nuc in 'ACGT':
            nnuc=float(col.count(nuc))
            lencol=float(len(col))
            tmpprof.append(nnuc / lencol)
        profile.append(tmpprof)
    #profile=  [[float(col.count(nuc)) / float(len(col)+4) for nuc in 'ACGT'] for col in columns]

    return (profile)

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

def score(motifs):
    columns = [''.join(seq) for seq in zip(*motifs)]
    max_count = sum([max([c.count(nucleotide) for nucleotide in 'ACGT']) for c in columns])
    return len(motifs[0])*len(motifs) - max_count

totentropy=0

prof=profile(mtrx)
print(prof)
prof=profile_pseudocount(mtrx)
print(prof)