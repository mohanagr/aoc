with open('dec23.txt') as f:
    lines=f.read().strip().split('\n')

import numpy as np
import heapq
arr = np.zeros((len(lines),len(lines[0])),dtype=bool)
newarr = np.zeros((len(lines),len(lines[0]),4),dtype=bool)
node_values = -np.ones((len(lines),len(lines[0]))) * 1
scoord=None
for i,line in enumerate(lines):
    for j,c in enumerate(list(line)):
        if lines[i][j] != '#':
            arr[i,j]=True
scoord = [0,1]
node_values[0,1]=0
np.set_printoptions(threshold=1000000,linewidth=1000)
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

int2str = lambda x,y,d: str(x)+'_'+str(y)+'_'+str(d)
str2int = lambda str: [int(a) for a in str.split('_')]
root=int2str(scoord[0],scoord[1],1)
# heapq.heappush(pq,(0,root))
stack = []
stack.append(root)
visited = set()
niter = 0

node_list = []
#node_list sort
while stack:
    curnode = stack.pop()
    # if niter > 10: break
    row,col,dirn = str2int(curnode)
    newarr[row,col,dirn] = True
    visited.add(str(row)+'_'+str(col))
    node_list.append(int2str(row,col,dirn))
    # print("popped", curnode)
    nes = get_neighbours(row,col,dirn,lines)
    # print(nes)
    for (r1,c1,d1) in nes:
        if not arr[r1,c1]:
            continue
        ne_id = int2str(r1,c1,d1)
        # print(ne_id)
        if str(r1)+'_'+str(c1) in visited:
            continue
        stack.append(ne_id)
    niter+=1
# print(node_list)
# print(newarr)
    
def dfs(curnode,topo,visited):
    row,col,dirn = str2int(curnode)
    visited[row,col] = True
    print("popped", curnode)
    nes = get_neighbours(row,col,dirn,lines)
    # if row == 5 and col ==4:
    #     print("dir is",dirn)
    #     print('neigh are', nes)
    #     exit(1)
    for (r1,c1,d1) in nes:
        if newarr[r1,c1,d1] and not visited[r1,c1]:
            ne_id = int2str(r1,c1,d1)
            dfs(ne_id,topo,visited)
    topo.append(str(row)+'_'+str(col))

topo = []
visited = np.zeros((len(lines),len(lines[0])),dtype=bool)
for node in node_list:
    row,col,dirn = str2int(node)
    if not visited[row,col]:
        dfs(node,topo,visited)
topo = topo[::-1]
print(topo)

for i,node in enumerate(topo):
    if i == 0: continue
    row,col= str2int(node)
    p_nodes = topo[max(i-4,0):i]
    # print(list(map(str2int,p_nodes)))   
    p_vals = [node_values[r,c] for (r,c) in map(str2int,p_nodes)]
    # print(p_vals)
    dist = max(p_vals) + 1
    # print(dist)
    if dist > node_values[row,col]:
        node_values[row,col] = dist
print(node_values.astype(int))
# while stack:
#     curnode = stack.pop()
#     # if niter > 10: break
#     # visited.add(curnode)
#     row,col,dirn = str2int(curnode)
#     # print(type(dirn))
#     # if curdist > node_values[row,col]: #we have a known better path
#     #     continue
#     # print("popped", curnode)
#     nes = get_neighbours(row,col,dirn,lines)
#     for (r1,c1,d1) in nes:
#         if not arr[r1,c1]:
#             continue
#         ne_id = int2str(r1,c1,d1)
#         # if ne_id in visited:
#         #     continue
#         dist = arr[r1,c1] + node_values[row,col]
#         # print("dist for neigh",ne_id, dist)
#         if dist > node_values[r1,c1]:
#             # print("shorter path found for",ne_id,"of", dist)
#             node_values[r1,c1] = dist
#             # node_parents[ne_id] = curnode
#             # print(node_parents)
#         stack.append(ne_id)
#     niter+=1
# print(node_values.astype(int))