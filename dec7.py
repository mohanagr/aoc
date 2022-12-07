class Tree:
    def __init__(self, name='root', data=None, children=None, parent=None):
        self.name = name
        self.parent = parent
        self.data = data
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)
    def get_child(self,name):
        for child in self.children:
            if child.name==name:
                return child

def print_tree(node):
    print("inside print tree")
    print(node.name,node.data)
    if(len(node.children)==0):
        return
    else:
        for child in node.children:
            # print(child.name)
            print_tree(child)

global dir_sums
dir_sums=[]


def assign_dir_totals(node):
    global dir_sums
    # print("inside print tree")
    # print(node.name)
    if(len(node.children)==0):
        return node.data
    else:
        s=0
        for child in node.children:
            # print(child.name)
            s+=assign_dir_totals(child)
        node.data=s
        dir_sums.append(s)
        return s


with open('temp.txt') as f:
    x=f.read().strip().split('\n')

root = Tree(name='/')
curnode = root
for l in x:
    tags = l.split(' ')
    # print(tags)
    # print("Current node and its parent is", curnode.name,curnode.parent)
    if(tags[0]=='$'): #it's a command
        if(tags[1]=='cd'):
            # add as node
            if(tags[2]=='..'):
                curnode = curnode.parent
            else:
                curnode = curnode.get_child(tags[2])
        elif(tags[1]=='ls'):
            #add the upcoming output as children of the current node
            pass
    else:
        if(tags[0]=='dir'):
            data=0
        else:
            data = int(tags[0])
        # print(data,"is data")
        curnode.add_child(Tree(name=tags[1],data=data,parent=curnode))

assign_dir_totals(root)
import numpy as np
dir_sums=np.asarray(dir_sums)
space_used = root.data
cur_free_space = 70000000-space_used
space_needed = 30000000-cur_free_space
print('------------------------------------')
print("Part 1",np.sum(dir_sums[dir_sums<=100000]))
print("------------------------------------")
print("------------------------------------")
print(space_needed)
print("Part 2", dir_sums[dir_sums>=space_needed].min())
# print_tree(root)