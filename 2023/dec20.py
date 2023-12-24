with open('dec20.txt') as f:
    lines=f.read().strip().split('\n')

class Node():
    def __init__(self,name):
        self.name = name
        self.type=None
        self.children = []
        self.parents = []
        self.state = None
        self.pulse = None #output puls

    def add_child(self,child):
        self.children.append(child)
    
    def add_parent(self,parent):
        self.parents.append(parent)
    
    def init_state(self):
        if self.type == '%':
            self.state = False
        elif self.type == '&':
            self.state = {}
            for p in self.parents:
                print(p.name)
                self.state[p.name]=False
    
    def tx_pulse(self, val):
        # send to processor pulses to all children
        if val is not None:
            pulses = []
            for child in self.children:
                pulses.append(self.name+'_'+child.name+'_'+str(int(val)))
            return pulses
    
    def rx_pulse(self, src, val):
        pulses = []
        to_send = None
        if self.type == '%':
            if val is False: #low pulse rx. flip state
                self.state = not self.state
                to_send = self.state
        elif self.type == '&':
            self.state[src] = val
            if all(self.state.values()):
                #all high states. send low pulse
                to_send = False
            else:
                to_send = True
        elif self.type == 'broadcaster':
            to_send = False
        
        return self.tx_pulse(to_send)




import graphviz
import matplotlib.pyplot as plt


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
        print('---------------------------------------------------------------')
        for node in self.nodes.values():
            children_names = [child.name for child in node.children]
            print(f"{node.name} (Type: {node.type}, State: {node.state}) -> {children_names}")
        print('---------------------------------------------------------------')   
    def init_state(self):
        for node in self.nodes.values():
            node.init_state()
    
    def check_state(self):
        # should the button pushing continue?
        flag = False
        for node in self.nodes.values():
            if node.type == '%':
                if node.state == True: #all should be false
                    flag = True
            elif node.type == '&':
                if any(node.state.values()): #all should be False
                    flag = True 
        return flag

sg1 = []
sg2 = []
sg3 = []
sg4 = []
    

g = Graph()
# dot = graphviz.Digraph('round-table', comment='The Round Table')

for line in lines:
    node,childs = line.split('->')
    node=node.strip()
    childs=childs.strip()
    childs = childs.split(',')
    # print(childs.split(','))
    if node=='broadcaster':
        ntype='broadcaster'
        parent=node
    else:
        ntype=node[0]
        parent=node[1:]
    # print(ntype,parent)
    g.add_node(parent)
    g.set_type(parent,ntype)
    for c in childs:
        c=c.strip()
        g.add_node(c)
        g.add_edge(parent,c)
g.init_state()
# g.display()
print("---------------------init state--------------------")
counter = {'1':0,'0':0}

# plt.figure(figsize=(15, 12))
# pos = nx.spring_layout(G, k=0.9, iterations=200)
# nx.draw(G, pos, with_labels=True,node_size=1000, labels=nx.get_node_attributes(G, 'label'))

# plt.show()

# for node in g.nodes.values():
#     dot.node(node.name, node.name+str(node.type))
#     for child in node.children:
#         dot.edge(node.name,child.name, constraint='false')



# dot.graph_attr['layout'] = 'fdp'
# dot.attr(size='30,30')
# # dot.attr(rankdir='LR')  # Left to Right, instead of Top to Bottom
# dot.attr('node', shape='box')
# dot.attr('graph', nodesep='1', ranksep='1')

# dot.render(directory='./').replace('\\', '/')

def pproc(puls):
    src,dest,val = puls.split('_')
    counter[val] +=1
    val = val == '1'
    return src,dest,val
global giga_flag
giga_flag = True
def push_button(g):
    global giga_flag
    root = 'button'
    q = ['button_broadcaster_0']

    visited = set()
    niter=0
    while q:
        # if niter>10: break
        # print(q)
        curpulse = q.pop()
        src,dest,val = pproc(curpulse)
        if dest == 'lg' and val == True:
            giga_flag = False
        
        newpulses = g.nodes[dest].rx_pulse(src,val)
        # print("current pulse", curpulse, src, dest, val)
        # print("queue is ", q)
        # print("new pulses", newpulses)
        if newpulses:
            for p in newpulses:
                q.insert(0,p)
        niter+=1

    # g.display()
# while(g.check_state()):
#     if(s%100==0):
#         print('puhsed ',s, " times")
#     if(s==1000):
#         break
#     push_button(g)
#     s+=1


#checks for &rb
mynodes = ['sj','kj','fk','xh','zs','ct','rt','hq','bb','kf','ph','hx']
# g.display()   

#part 2, for each sub-tree, check the convergence, multiply together for all trees.
ss=0
while(giga_flag):
    push_button(g)
    ss+=1
print(ss)

