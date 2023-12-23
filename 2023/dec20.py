with open('dec20.txt') as f:
    lines=f.read().strip().split('\n')

class Node():
    def __init__(self,name):
        self.name = name
        self.type=None
        self.children = []
        self.parents = []

    def add_child(self,child):
        self.children.append(child)
    
    def add_parent(self,parent):
        self.parents.append(parent)

class Graph():
    def __init__(self):
        self.nodes = {}

    def add_node(self,node_name):
        if node_name not in self.nodes:
            self.nodes[node_name] = Node(node_name)

    def add_edge(self,a,b):
        # assume that both nodes exist
        self.nodes[a].add_child(self.nodes[b])
        self.nodes[b].add_parent(self.nodes[a])
    
    def set_type(self,a,ntype):
        # avoid direct access to a Node instance.
        self.nodes[a].type = ntype

    def display(self):
        for node in self.nodes.values():
            children_names = [child.name for child in node.children]
            print(f"{node.name} (Type: {node.type}) -> {children_names}")

g = Graph()
for line in lines:
    node,childs = line.split('->')
    node=node.strip()
    childs=childs.strip()
    childs = childs.split(',')
    # print(childs.split(','))
    if node=='broadcaster':
        ntype=None
        parent=node
    else:
        ntype=node[0]
        parent=node[1:]
    # print(ntype,parent)
    g.add_node(parent)
    g.set_type(parent,ntype)
    for c in childs:
        # print(c)
        c=c.strip()
        g.add_node(c)
        g.add_edge(parent,c)
g.display()

root = 'broadcaster'
q = [root]

visited = set()
niter=0
while q:
    if niter>10: break
    print(q)
    curnode = q.pop()
    # do sth
    visited.add(curnode)
    print("current node", curnode)
    for node in g.nodes[curnode].children:
        if node.name not in q:
            q.insert(0,node.name)
    niter+=1

    