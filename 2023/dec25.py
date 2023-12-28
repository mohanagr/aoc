
import graphviz
import matplotlib.pyplot as plt
with open('dec25.txt') as f:
    lines=f.read().strip().split('\n')

all_nodes = set()
dot = graphviz.Graph('round-table')

for line in lines:
    source,children = line.split(':')
    source = source.strip()
    children = children.strip()
    children = children.split(' ')
    all_nodes.add(source)
    for child in children:
        all_nodes.add(child)

# print(all_nodes)
for node in all_nodes:
    dot.node(node)


for line in lines:
    source,children = line.split(':')
    source = source.strip()
    children = children.strip()
    children = children.split(' ')
    for child in children:
        dot.edge(source,child)

dot.graph_attr['layout'] = 'fdp'
dot.attr(size='30,30')
# dot.attr(rankdir='LR')  # Left to Right, instead of Top to Bottom
dot.attr('node', shape='box')
dot.attr('graph', nodesep='100', ranksep='10')

dot.render(directory='./').replace('\\', '/')