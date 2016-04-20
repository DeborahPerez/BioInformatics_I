import math

lst=[0.5,0,0,0.5] #1
lst=[0.25,0.25,0.25,0.25] #2
lst=[0,0,0,1] #0
lst=[0.25,0,0.5,0.25] #1.5
entropy=0

for i in lst:
    if i>0:
        entropy =(entropy+i*math.log2(i))

print(entropy*-1)