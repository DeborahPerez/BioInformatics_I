import sys
#2016 Jorge Canelhas
lines = sys.stdin.read().splitlines()
gene=lines[0]

skew=list()
currval=0
minval=10000
skew.append(currval)
for nuc in gene:
    if nuc=='C':
        currval=currval-1
    elif nuc=='G':
        currval=currval+1
    else:
        currval=currval
    skew.append(currval)
    if currval<minval:
        minval=currval

for n,i in enumerate(skew):
    print(i, end=" ")
print()
for n,i in enumerate(skew):
    if i==minval:
        print(n, end=" ")

    