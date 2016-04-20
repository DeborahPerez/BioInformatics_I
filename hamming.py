#2016 Jorge Canelhas
import sys

#lines = sys.stdin.read().splitlines()
#l1=lines[0]
#l2=lines[1]

l1='CTTGAAGTGGACCTCTAGTTCCTCTACAAAGAACAGGTTGACCTGTCGCGAAG'
l2='ATGCCTTACCTAGATGCAATGACGGACGTATTCCTTTTGCCTCAACGGCTCCT'
def HammingDistance(g1, g2):
    distance=0
    for i,j in zip(g1,g2):
        if i!=j:
            distance=distance+1
    return distance

print(HammingDistance(l1,l2))