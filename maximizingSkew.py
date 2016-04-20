import sys

#lines = sys.stdin.read().splitlines()
gene='GCATACACTTCCCAGTAGGTACTG'

skew=list()
currval=0
maxval=-10000
skew.append(currval)
for nuc in gene:
    if nuc=='C':
        currval=currval-1
    elif nuc=='G':
        currval=currval+1
    else:
        currval=currval
    skew.append(currval)
    if currval<maxval:
        maxval=currval

for n,i in enumerate(skew):
    print(i, end=" ")
print()
for n,i in enumerate(skew):
    if i==maxval:
        print(n, end=" ")

    