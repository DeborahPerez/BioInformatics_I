#2016 Jorge Canelhas

import sys

lines = sys.stdin.read().splitlines()
l1=lines[0]



def CumputePatternToNumber(pattern):
    dic={'A':0,'C':1,'G':2,'T':3}
    total=0
    for n,i in enumerate(pattern):
        l=len(pattern)-n
        total=total+(dic[i]*(4**(l-1)))
    return total

print(CumputePatternToNumber(l1))