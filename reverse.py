

import sys

lines = sys.stdin.read().splitlines()
l1=lines[0]
count=0
#l1='1234567890'

l2=''
for i in l1:
    if i=='A':
        l2=l2+'T'
    elif i=='T':
        l2=l2+'A'
    elif i=='G':
        l2=l2+'C'
    else:
        l2=l2+'G'
print (l1)
print (l2)
out=''
start=len(l2)-1
for i in range(start+1,0,-1):

    out=out+l2[i-1:i]


print()
print (out)
print()