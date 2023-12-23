with open('dec10.txt') as f:
    lines=f.read().strip().split('\n')
import re
myre = re.compile(r"S")
for i,line in enumerate(lines):
    m=list(myre.finditer(line))
    if len(m)>0:
        c,_=int(m[0].start()),int(m[0].end())
        r = i
    lines[i]= '.' + line + '.'

xx = ''.join(['.']*len(lines[0]))
lines.insert(0,xx)
lines.append(xx)
# print(lines)
# for line in lines:
#     print(line)
print(len(lines), len(lines[0]))
r+=1
c+=1
# print(lines[r][c])
class Nodes():
    def __init__(self, name=None, visited=None):
        self.name = name
        self.visited = visited
        self.next = None
    
def get_connected(current, neighbours):
    #lets go clockwise
    connected = []
    pts = []
    if neighbours[0] in ['|','F', '7','S'] and current in ['|','L', 'J','S']:
        connected.append(neighbours[0])
        pts.append('N')
    if neighbours[1] in ['-','7', 'J','S'] and current in ['-','L', 'F','S']:
        connected.append(neighbours[1])
        pts.append('E')
    if neighbours[2] in ['|','L', 'J','S'] and current in ['|','F', '7','S']:
        connected.append(neighbours[2])
        pts.append('S')
    if neighbours[3] in ['-','L', 'F','S'] and current in ['-','7', 'J','S']:
        connected.append(neighbours[3])
        pts.append('W')
    return pts

def get_neighbours(r,c, lines):
    W = lines[r][c-1]
    E = lines[r][c+1]
    S = lines[r+1][c]
    N = lines[r-1][c]
    return [N,E,S,W]

def dir2coord(r,c,dirs):
    for dirn in dirs:
        if dirn == 'N':
            return r-1,c
        if dirn == 'S':
            return r+1,c
        if dirn == 'E':
            return r,c+1
        if dirn == 'W':
            return r,c-1
import numpy as np
count=0
node_xy = np.zeros((15000,2),dtype='int') #X Y
#
node_xy[count,0]=c
node_xy[count,1]=r

nn = get_neighbours(r,c,lines)
current = lines[r][c]
# print("Current", current)
cn = get_connected(current,nn)
# print("nn", nn)
# print("cn", cn)
namer = lambda r, c: str(r)+"_"+str(c)
name = namer(r,c)
nodes = [name]
# print("nodes are", nodes)
# rootnode = Nodes(name=name,visited=True)
# rootnode.next = 
r,c = dir2coord(r,c,cn[0])
# print("starting loop with", r, c)


while(True):
    count+=1
    node_xy[count,0]=c
    node_xy[count,1]=r
    name = namer(r,c)
    nodes.append(name) #mark the cur node as visited
    current = lines[r][c]
    #get next neighbours
    nn = get_neighbours(r,c,lines)
    cn = get_connected(current, nn)
    # print("nn", nn)
    # print("cn", cn)
    assert(len(cn)==2)
    r1,c1 = dir2coord(r,c,cn[0])
    new1 = namer(r1,c1)
    r2,c2 = dir2coord(r,c,cn[1])
    new2 = namer(r2,c2)
    # print("two nodes connected are:", lines[r1][c1], lines[r2][c2])
    if new1 in nodes and new2 in nodes:
        # both visited = we've completed a loop
        # print("ending the loop")
        break
    elif new1 in nodes:
        r,c = r2,c2 # go to the univisted node
        # print("moving to", lines[r2][c2])
    else:
        r,c = r1,c1
        # print("moving to", lines[r1][c1])
print("total steps taken", len(nodes), (count+1)/2)

mapshape = np.asarray([len(lines),len(lines[0])])
mymap = np.zeros(3*mapshape,dtype=int)
N = len(nodes)
node_xy[N,:] = node_xy[0,:]
# xy = node_xy[:N+1,:].copy()
# area = 0.5*np.sum(xy[:-1,0]*xy[1:,1] - xy[1:,0]*xy[:-1,1]) #green's theorem or shoelace formula
# inside = (area- N/2 + 1) #picks theorem
# print("area is ",area, "points inside", inside)

#following is BFS floodfill solution. took a bit too long to converge

for i in range(N+1):
    x1,y1 = node_xy[i,:]
    x2,y2 = node_xy[i+1,:]
    # print(x1,y1,x2,y2)
    xn1,yn1 = 3*x1+1, 3*y1+1
    xn2,yn2 = 3*x2+1, 3*y2+1
    # xn1,yn1 = x1+1, y1+1
    # xn2,yn2 = x2+1, y2+1
    # print(xn1,yn1,xn2,yn2)
    if(xn1>xn2):
        mymap[yn1:yn2+1, xn2:xn1+1]=1
    elif(yn1>yn2):
        mymap[yn2:yn1+1, xn1:xn2+1]=1
    else:
        mymap[yn1:yn2+1, xn1:xn2+1]=1
np.set_printoptions(threshold=1000000)
# print(mymap)
print("S is at", node_xy[0]*3) #start from right
for row in range(mymap.shape[0]):
    print(''.join([str(a) for a in mymap[row,:]]))
print("\n\n")

# ready for flood fill
# all filled points % 3 ==1 were present in original map.

rootnode = [15,5] #row, col
# rootnode = [10,10]
queue = []
queue.insert(0,rootnode)
niter=0
while(len(queue)>0):
    if niter>1000000:
        break
    curnode = queue.pop()
    # print("cur node is", curnode, "value is", mymap[curnode[0],curnode[1]])
    if mymap[curnode[0],curnode[1]]==0:
        mymap[curnode[0],curnode[1]]=2 #change color
    
    if curnode[0] < 0 or curnode[1] < 0:
        print("done fucked up")
        break
    if mymap[curnode[0]+1,curnode[1]] == 0:
        queue.insert(0,[curnode[0]+1,curnode[1]])
    if mymap[curnode[0],curnode[1]+1] == 0:
        queue.insert(0,[curnode[0],curnode[1]+1])
    if mymap[curnode[0]-1,curnode[1]] == 0:
        queue.insert(0,[curnode[0]-1,curnode[1]])
    if mymap[curnode[0],curnode[1]-1] == 0:
        queue.insert(0,[curnode[0],curnode[1]-1])
    niter+=1
# print(niter)
# for row in range(mymap.shape[0]):
#     print(''.join([str(a) for a in mymap[row,:]]))

for row in range(mymap.shape[0]):
    print(''.join([str(a) for a in mymap[row,:]]))
print("\n\n")

    
