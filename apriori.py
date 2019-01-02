import pandas as pd
import numpy as np
import itertools
from functools import reduce
import matplotlib.pyplot as plt
data=pd.read_csv('data.txt',delimiter=' ')
set=data['data']
large=[]
subset=[list(x) for x in set.values]
print("DATA SET:")
for i in subset:
    while ',' in i:
        i.remove(',')
    print(i)
large=reduce((lambda x,y: x+y),subset)
elements=np.unique(large)
print("All products:")
print(elements)
product_count=[0 for i in range (0,len(elements))]
for i in range(0,len(elements)):
    for j in subset:
        product_count[i]=product_count[i]+j.count(elements[i])
for i in range(0,len(product_count)):
        if product_count[i]<3:
            product_count[i]=0
while 0 in product_count:
    ind=product_count.index(0)
    del product_count[ind]
    del elements[ind]
for i in range(0,len(product_count)):
    print(elements[i],end='')
    print(" --> ",end='')
    print(product_count[i])
pair2=list(itertools.combinations(elements,2))
ar2_count=[0 for i in range (0,len(pair2))]
for i in range (0,len(pair2)):
    for j in subset:
        if pd.Series(pair2[i]).isin(j).all():
            ar2_count[i]=ar2_count[i]+1
for i in range(0,len(ar2_count)):
        if ar2_count[i]<3:
            ar2_count[i]=0
while 0 in ar2_count:
    ind=ar2_count.index(0)
    del ar2_count[ind]
    del pair2[ind]
print(" FOR TAKING 2 AT A TIME")
for i in range(0,len(ar2_count)):
    print(pair2[i],end='')
    print(" --> ",end='')
    print(ar2_count[i])
pair=pair2
q=1
pair_new=[]
while(len(pair)>1):
    print(" FOR TAKING "+str(q+2)+" AT A TIME")
    for i in range(0,len(pair)):
        for j in range(i+1,len(pair)-1):
            if  np.all(pair[i][0:q]==pair[j][0:q]):
                #print(str(pair[i])+str(pair[j]))
                pair_new.append(list(np.unique(np.concatenate((pair[i],pair[j])))))
    ar_count=[0 for i in range (0,len(pair_new))]
    for i in range (0,len(pair_new)):
        for j in subset:
            if pd.Series(pair_new[i]).isin(j).all():
                ar_count[i]=ar_count[i]+1
    for i in range(0,len(ar_count)):
            if ar_count[i]<3:
                ar_count[i]=0
    while 0 in ar_count:
        ind=ar_count.index(0)
        del ar_count[ind]
        del pair_new[ind]
    for i in range(0,len(ar_count)):
        print(pair_new[i],end='')
        print(" --> ",end='')
        print(ar_count[i])
    pair=np.array(pair_new)
    count=np.array(ar_count)
    while ar_count:
        del ar_count[0]
        del pair_new[0]
    q=q+1
