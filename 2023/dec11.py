with open('dec11.txt') as f:
    lines=f.read().strip().split('\n')
import re
import numpy as np
arr = np.zeros((len(lines),len(lines[0])),dtype=int)
myre = re.compile(r"#")
for i,line in enumerate(lines):
    m=list(myre.finditer(line))
    if len(m)>0:
        for match in m:
            c,_=int(match.start()),int(match.end())
            r = i
            arr[r,c]=1
    # lines[i]= '.' + line + '.'
np.set_printoptions(threshold=1000000)
print(arr.shape)

rowidx = []
colidx = []
# newarr = arr[0,:].copy()
for i in range(1,arr.shape[0]):
    # newarr = np.vstack([newarr,arr[i,:]])
    if np.sum(arr[i,:]) == 0:
        rowidx.append(i)
        # newarr = np.vstack([newarr,np.zeros((1,newarr.shape[1]),dtype=newarr.dtype)])
# print(newarr)

for i in range(1,arr.shape[1]):
    # newarr = np.vstack([newarr,arr[i,:]])
    if np.sum(arr[:,i]) == 0:
        colidx.append(i)

rowidx = np.asarray(rowidx)
colidx = np.asarray(colidx)
# arr = newarr.copy()

# newarr = arr[:,0:1].copy()
# print(newarr.shape,arr.shape)
# for i in range(1,arr.shape[1]):
#     newarr = np.hstack([newarr,arr[:,i:i+1]])
#     if np.sum(arr[:,i]) == 0:
#         newarr = np.hstack([newarr,np.zeros((newarr.shape[0],1),dtype=newarr.dtype)])

# print(newarr.shape)


x,y = np.where(arr==1)
s=0
N = len(x)
delta=1000000-1
for i in range(N):
    for j in range(i+1,N):
        x1,y1 = x[i],y[i]
        x2,y2 = x[j],y[j]
        dist = np.abs(x1-x2) + np.abs(y1-y2)
        nx = len(rowidx[(rowidx>min(x1,x2))&(rowidx<max(x1,x2))])
        ny = len(colidx[(colidx>min(y1,y2))&(colidx<max(y1,y2))])
        if nx > 0:
            dist+=(delta*nx)
        if ny > 0:
            dist+=(delta*ny)
        s+=dist
        # print(f"Pair: [{x1},{y1}]-[{x2},{y2}], dist: {dist}")
print(s)