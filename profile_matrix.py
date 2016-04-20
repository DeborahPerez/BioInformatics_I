mtrx=['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA','GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG','TAGTACCGAGACCGAAAGAAGTATACAGGCGT','TAGATCAAGTTTCAGGTGCACGTCGGTGAACC','AATCCACCAGCTCCACGTGCAATGTTGGCCTA']
mtrx=['TCGGGGGTTTTT','CCGGTGACTTAC','ACGGGGATTTTC','TTGGGGACTTTT','AAGGGGACTTCC','TTGGGGACTTCC','TCGGGGATTCAT','TCGGGGATTCCT','TAGGGGAACTAC','TCGGGTATAACC']
# CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA
# GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG
# TAGTACCGAGACCGAAAGAAGTATACAGGCGT
# TAGATCAAGTTTCAGGTGCACGTCGGTGAACC
# AATCCACCAGCTCCACGTGCAATGTTGGCCTA



import math

def calcentropy(lst):
    entropy = 0

    for i in lst:
        if i > 0:
            entropy = (entropy + i * math.log(i,2))
    return (entropy * -1)



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

print (profile)

for l in count:
    print (l)

totentropy=0
for l in profile:
    print (calcentropy(l))

    totentropy+=calcentropy(l)
print('----')
print(totentropy)