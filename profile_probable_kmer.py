# import sys
#
# lines = sys.stdin.read().splitlines()
# l1=lines[0]
# l2=lines[1]
#
# l3=list()
# for i in lines[2].split(' '):
#     l3.append(float(i))
# l4=list()
# for i in lines[3].split(' '):
#     l4.append(float(i))
# l5=list()
# for i in lines[4].split(' '):
#     l5.append(float(i))
# l6=list()
# for i in lines[5].split(' '):
#     l6.append(float(i))

l1='ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT'
l2=5
l3=[0.2,0.2,0.3,0.2,0.3]
l4=[0.4,0.3,0.1,0.5,0.1]
l5=[0.3,0.3,0.5,0.2,0.4]
l6=[0.1,0.2,0.1,0.1,0.2]


l1='AAGTTC'
l2=6
l3=[0.2,0.2,0.3,0.2,0.3]
l4=[0.4,0.3,0.1,0.5,0.1]
l5=[0.3,0.3,0.5,0.2,0.4]
l6=[0.1,0.2,0.1,0.1,0.2]
l3=[0.303,0.227,0.333,0.303,0.242,0.212,0.167,0.288,0.212,0.197,0.258,0.273,0.242,0.242,0.242]
l4=[0.288,0.318,0.273,0.303,0.303,0.424,0.273,0.242,0.258,0.227,0.288,0.258,0.242,0.242,0.242]
l5=[0.258,0.227,0.152,0.182,0.242,0.197,0.333,0.258,0.303,0.242,0.167,0.288,0.288,0.227,0.273]
l6=[0.152,0.227,0.242,0.212,0.212,0.167,0.227,0.212,0.227,0.333,0.288,0.182,0.227,0.288,0.242]

l3=[0.4,0.3,0.0,0.1,0.0,0.9]
l4=[0.2,0.3,0.0,0.4,0.0,0.1]
l5=[0.1,0.3,1.0,0.1,0.5,0.0]
l6=[0.3,0.1,0.0,0.4,0.5,0.0]


l2=int(l2)
mtrx=[l3,l4,l5,l6]

def profileprobkmer(dna,size,mtrx):
    print()
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
result=profileprobkmer(l1,l2,mtrx)
print(result)