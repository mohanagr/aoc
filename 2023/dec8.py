class Graph():
    def __init__(self):
        self.graph = {}

    def add_edge(self,node, left, right):
        self.graph[node] = [left, right]
import re
with open('dec8.txt') as f:
    cmd, edges=f.read().strip().split('\n\n')
myre = re.compile(r"[0-9A-Z]+")
g=Graph()
mp = {'L':0,'R':1}
cur_nodes = []
for e in edges.split("\n"):
    # print(e)
    node,left,right = myre.findall(e)
    g.add_edge(node,left,right)
    if node[2]=='A':
        cur_nodes.append(node)
# print(g.graph)
# cur_node='AAA'
count=0
flag=1
next_nodes = []
print(cur_nodes)
# exit()
for cur_node in cur_nodes:
    count = 0
    flag = 1
    while(flag):
        for c in cmd:
            if cur_node[2]=='Z':
                flag=0
                break
            cur_node = g.graph[cur_node][mp[c]]
            count+=1
    print(cur_node, count)


