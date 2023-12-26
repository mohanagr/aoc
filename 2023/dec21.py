with open('dec21.txt') as f:
    lines=f.read().strip().split('\n')

import numpy as np
import heapq
arr = np.zeros((len(lines),len(lines[0])),dtype=bool)
visited = arr.copy()
node_values = np.ones((len(lines),len(lines[0]))) * np.inf
scoord=None
for i,line in enumerate(lines):
    for j,c in enumerate(list(line)):
        if lines[i][j]=='.':
            arr[i,j]=True
        if lines[i][j]=='S':
            arr[i,j]=True
            scoord = [i,j]
np.set_printoptions(threshold=1000000)
# print(arr.astype(int))
print(scoord)
nr,nc = arr.shape
def get_neighbours(r,c,nr=nr,nc=nc):
    N=[r-1,c]
    E=[r,c+1]
    S=[r+1,c]
    W=[r,c-1]
    res=[]
    if r > 0:
        res.append(N)
    if r < nr-1:
        res.append(S)
    if c < nc-1:
        res.append(E)
    if c > 0:
        res.append(W)
    return res

pq = []

int2str = lambda x,y: str(x)+'_'+str(y)
str2int = lambda str: [int(a) for a in str.split('_')]
root=int2str(scoord[0],scoord[1])
heapq.heappush(pq,(0,root))
visited = set()
niter = 0
while pq:
    curdist, curnode = heapq.heappop(pq)
    visited.add(curnode)
    row,col = str2int(curnode)
    if curdist > node_values[row,col]: #we have a known better path
        continue
    # print("popped", curnode, curdist)
    nes = get_neighbours(row,col)
    # print(nes)
    for (r1,c1) in nes:
        if not arr[r1,c1]:
            continue
        ne_id = int2str(r1,c1)
        if ne_id in visited:
            continue
        dist = arr[r1,c1] + curdist
        if dist < node_values[r1,c1]:
            # print("shorter path found for",ne_id,"of", dist)
            node_values[r1,c1] = dist
            # node_parents[ne_id] = curnode
            # print(node_parents)
            heapq.heappush(pq,(dist,ne_id))
    niter+=1
# print(node_values)
print(np.sum(node_values[node_values<=14]%2==0))
# print(np.where((node_values<=6)&(node_values%2==0)))
# print(np.sum(node_values==64))