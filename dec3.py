import numpy as np

# def getval(x):
#     v=ord(x)
#     if(v<97):
#         return v-64+26
#     else:
#         return v-96


def assignarray(mystr,arr):
    arr[[ord(ch) for ch in mystr]]=1
    return arr

# s=0
# for l in x:
#     mylen = len(l)
#     # print(l)
#     for i in range(0,mylen//2):
#         if l[i] in l[mylen//2:]:
#             # print("common letter is", l[i])
#             s += getval(l[i])
#             break

# print("Total is ", s)
import time
with open('dec3input.txt') as f:
    x=f.read().split('\n')

# t1=time.time()
# s=0
# myarr=np.empty(200)
# for lines in zip(x[0::3],x[1::3],x[2::3]):
#     myarr[:]=0
#     myarr[[ord(ch) for ch in lines[0]]]+=1
#     myarr[[ord(ch) for ch in lines[1]]]+=1
#     myarr[[ord(ch) for ch in lines[2]]]+=1
#     myarr[:]=myarr//3
#     ix=np.where(myarr==1)[0][0]
#     s+=(ix-38 if ix<97 else ix-96)
# print(s)
# t2=time.time()
# print(t2-t1)

s=sum(map(lambda ix: ix-38 if ix<97 else ix-96, [ord(set(lines[0]).intersection(set(lines[1])).intersection(set(lines[2])).pop()) for lines in zip(x[0::3],x[1::3],x[2::3])]))
print(s)
t2=time.time()
print(t2-t1)

# Simon's Solution

with open("dec3input.txt") as f:
    sl = f.readlines()
import string
from functools import reduce
t1=time.time()
print("part 2:",sum([(list(string.ascii_lowercase) + list(string.ascii_uppercase)).index(list(reduce(lambda x,y: x.intersection(y),map(lambda x: set(list(x.strip())), line_set)))[0]) + 1 for line_set in zip(sl[0::3], sl[1::3], sl[2::3])]))
t2=time.time()
print(t2-t1)