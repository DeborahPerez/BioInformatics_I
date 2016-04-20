gene = 'GAGCCACCGCGATA'
skew=list()
currval=0
skew.append(currval)
for nuc in gene:

    if nuc=='C':
        currval=currval-1
    elif nuc=='G':
        currval=currval+1
    else:
        currval=currval
    skew.append(currval)
for i in skew:
    print(i, end=" ")
