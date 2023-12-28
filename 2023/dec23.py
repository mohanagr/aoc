with open('dec23.txt') as f:
    lines=f.read().strip().split('\n')

import numpy as np
import heapq
arr = np.zeros((len(lines),len(lines[0])),dtype=int)
visited = arr.copy()
node_values = -np.ones((len(lines),len(lines[0]))) * 1
scoord=None
for i,line in enumerate(lines):
    for j,c in enumerate(list(line)):
        if lines[i][j] != '#':
            arr[i,j]=1
scoord = [0,1]
node_values[0,1]=0
np.set_printoptions(threshold=1000000)
print(arr.astype(int))
print(scoord)
nr,nc = arr.shape
def get_neighbours(r,c,d,lines,nr=nr,nc=nc):
    N=[r-1,c,0]
    E=[r,c+1,1]
    S=[r+1,c,2]
    W=[r,c-1,3]
    res=[]
    char = lines[r][c]
    # print("received ne request", r,c, d, char, type(d))
    # if char == "v":
    #     res.append(S)
    #     return res
    # if char == ">":
    #     res.append(E)
    #     return res
    if r > 0 and d!=2:
        # if lines[r-1][c] != 'v':
        res.append(N)
    if r < nr-1 and d!=0:
        res.append(S)
    if c < nc-1 and d!=3:
        res.append(E)
    if c > 0 and d!=1:
        # if lines[r][c-1] != '>':
        res.append(W)
    return res

pq = []

int2str = lambda x,y,d: str(x)+'_'+str(y)+'_'+str(d)
str2int = lambda str: [int(a) for a in str.split('_')]
root=int2str(scoord[0],scoord[1],1)
# heapq.heappush(pq,(0,root))
stack = []
stack.append(root)
# visited = set()
niter = 0
while stack:
    curnode = stack.pop()
    # if niter > 10: break
    # visited.add(curnode)
    row,col,dirn = str2int(curnode)
    # print(type(dirn))
    # if curdist > node_values[row,col]: #we have a known better path
    #     continue
    # print("popped", curnode)
    nes = get_neighbours(row,col,dirn,lines)
    for (r1,c1,d1) in nes:
        if not arr[r1,c1]:
            continue
        ne_id = int2str(r1,c1,d1)
        # if ne_id in visited:
        #     continue
        dist = arr[r1,c1] + node_values[row,col]
        # print("dist for neigh",ne_id, dist)
        if dist > node_values[r1,c1]:
            # print("shorter path found for",ne_id,"of", dist)
            node_values[r1,c1] = dist
            # node_parents[ne_id] = curnode
            # print(node_parents)
        stack.append(ne_id)
    niter+=1
print(node_values.astype(int))