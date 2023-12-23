with open('dec17.txt') as f:
    lines=f.read().strip().split('\n')
import heapq
import numpy as np
arr=np.zeros((len(lines),len(lines[0])))
for i,line in enumerate(lines):
    arr[i,:] = np.asarray([int(x) for x in list(line)])

nr,nc = arr.shape
np.set_printoptions(threshold=1000000)
# print(arr)

class Node:
    def __init__(self,name,value=None,fwlen=None,parent=None):
        self.name = name
        self.value = value
        self.fwlen = fwlen
        self.parent = parent
        self.children = []
    
    def __lt__(self,other):
        return False
    
    def add_children(self,children):
        for child in children:
            self.children.append[child]

#d: 0=up 1=right 2=down 3=left
# def get_neighbours(r,c,n,d,nr=nr,nc=nc):
#     N=[r-1,c,1,0]
#     E=[r,c+1,1,1]
#     S=[r+1,c,1,2]
#     W=[r,c-1,1,3]
#     if d==0:
#         N[2]=n+1
#     elif d==1:
#         E[2]=n+1
#     elif d==2:
#         S[2]=n+1
#     else:
#         W[2]=n+1
#     res=[]
#     if r > 0 and N[2]<=3 and d!=2:
#         res.append(N)
#     if r < nr-1 and S[2]<=3 and d!=0:
#         res.append(S)
#     if c < nc-1 and E[2]<=3 and d!=3:
#         res.append(E)
#     if c > 0 and W[2]<=3 and d!=1:
#         res.append(W)
#     return res

def get_neighbours(r,c,n,d,nr=nr,nc=nc):
    N=[r-1,c,1,0]
    E=[r,c+1,1,1]
    S=[r+1,c,1,2]
    W=[r,c-1,1,3]
    Nf,Ef,Sf,Wf = True,True,True,True
    if d==0:
        N[2]=n+1
    elif d==1:
        E[2]=n+1
    elif d==2:
        S[2]=n+1
    else:
        W[2]=n+1
    res=[]
    if r > 0 and N[2]<=10 and d!=2:
        if d in (1,3):
            if n >= 4: #turn only if you've been walking in same dir for 4
                res.append(N)
        else:
            res.append(N)
    if r < nr-1 and S[2]<=10 and d!=0:
        if d in (1,3):
            if n >= 4: #turn only if you've been walking in same dir for 4
                res.append(S)
        else:
            res.append(S)
    if c < nc-1 and E[2]<=10 and d!=3:
        if d in (0,2):
            if n >= 4: #turn only if you've been walking in same dir for 4
                res.append(E)
        else:
            res.append(E)
    if c > 0 and W[2]<=10 and d!=1:
        if d in (0,2):
            if n >= 4: #turn only if you've been walking in same dir for 4
                res.append(W)
        else:
            res.append(W)
    return res
            

pq = []
node_values = np.ones((arr.shape[0],arr.shape[1],11,4),dtype='int32')*np.inf
node_values[0,0,0,1]=0
# node_parents = {'0_0':None}
root = '0_0_0_1'
heapq.heappush(pq,(0,root))
int2str = lambda x,y,n,d: str(x)+'_'+str(y)+'_'+str(n)+'_'+str(d)
str2int = lambda str: [int(a) for a in str.split('_')]
niter=0
while pq:
    # if(niter>20): break 
    curdist, curnode = heapq.heappop(pq)
    row,col,n,d = str2int(curnode)
    if curdist > node_values[row,col,n,d]: #we have a known better path
        continue
    if row == nr-1 and col == nc-1 and n <=10 and n >=4: #reached the target node
        break
    # print("popped", curnode, curdist)
    nes = get_neighbours(row,col,n,d)
    # print(nes)
    for (r1,c1,n1,d1) in nes:
        ne_id = int2str(r1,c1,n1,d1)
        # print(node_parents, ne_id)
        # if ne_id in node_parents.keys():
        #     # print(curnode.parent.name, "parent")
        #     # print("parent of ne is", node_parents[curnode])
        #     if ne_id == node_parents[curnode]:
        #         # print("not looking at the parent")
        #         continue
        # print("checking ne",r1,c1,n1,d1)
        dist = arr[r1,c1] + curdist
        if dist < node_values[r1,c1,n1,d1]:
            # print("shorter path found for",ne_id,"of", dist)
            node_values[r1,c1,n1,d1] = dist
            # node_parents[ne_id] = curnode
            # print(node_parents)
            heapq.heappush(pq,(dist,ne_id))
    niter+=1

print("finished with", curdist)

# while(node_parents[curnode]):
#     print(curnode)
#     curnode = node_parents[curnode]