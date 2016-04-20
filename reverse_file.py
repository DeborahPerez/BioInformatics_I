

f=open('dataset_3_2.txt','r')
l1=f.readline().strip()
count=0
#l1='1234567890'


def reverse_complement(gene):
    tmp=''
    for i in gene:
        if i=='A':
            tmp=tmp+'T'
        elif i=='T':
            tmp=tmp+'A'
        elif i=='G':
            tmp=tmp+'C'
        else:
            tmp=tmp+'G'
    out=''
    start=len(tmp)-1
    for i in range(start+1,0,-1):

        out=out+l2[i-1:i]
    return out


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
print (reverse_complement(l1))
print()