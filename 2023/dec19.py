import re

def parse_input(input_text):
    # Define the pattern to match the required structure
    pattern = r"(\w+)\{([^}]*)\}"
    
    # Find all matches
    matches = re.findall(pattern, input_text)

    parsed_data = {}
    for match in matches:
        key = match[0]  # The word before the curly braces
        elements = match[1].split(',')  # Splitting the elements inside the curly braces

        element_details = []
        for element in elements:
            # Splitting each element into its components (if present)
            element_parts = re.split(r'([<>]=?|\:)', element)
            element_name = element_parts[0].strip()
            if len(element_parts) > 1:
                comparison = element_parts[1].strip()
                number = element_parts[2].strip()
                next_element = element_parts[4].strip()
                element_details.append((next_element, element_name, comparison, number))
            else:
                element_details.append((element_name,))

        parsed_data[key] = element_details

    return parsed_data

def update_ranges(range, condition, number):
    # print(range,condition,number)
    number = int(number)
    new_range = []
    out_range = []
    range_start, range_end = range[:]
    if condition == '>':
        new_start = max(range_start, number + 1)
        new_range = [new_start, range_end]
        out_range = [range_start, number]
    elif condition == '<':
        new_end = min(range_end, number - 1)
        new_range = [range_start, new_end]
        out_range = [number, range_end]

    return new_range, out_range

with open('dec19.txt') as f:
    node_lines, parts=f.read().strip().split('\n\n')
import operator
ops = {
        ">": operator.gt,
        "<": operator.lt,
        ">=": operator.ge,
        "<=": operator.le,
        "==": operator.eq,
        "!=": operator.ne,
    }
graph= parse_input(node_lines)

# print(graph)
pattern = r"x=(\d+),m=(\d+),a=(\d+),s=(\d+)"
# numA=0
# numR=0
# xmas=0
# for line in parts.split("\n"):
#     # Search for the pattern in the input string
#     match = re.search(pattern, line)
#     part_dict = {'x':int(match.group(1)),'m':int(match.group(2)), 'a':int(match.group(3)), 's':int(match.group(4))}

#     curnode = 'in'
#     while(True):
#         # print("curnode is", curnode)
#         if curnode == 'A':
#             numA+=1
#             xmas += part_dict['x']+part_dict['m']+part_dict['a']+part_dict['s']
#             break
#         elif curnode == 'R':
#             numR +=1 
#             break
#         for child in graph[curnode]:
#             # print('looking at child', child[0])
#             if len(child) == 1: #no comparisons
#                 curnode = child[0]
#                 break
#             else:
#                 # print(child)
#                 if ops[child[2]](part_dict[child[1]],int(child[3])):
#                     curnode = child[0]
#                     break

# print(xmas)

def comb_from_range(xmas):
    # print("range passed to A", xmas)
    return (xmas['x'][1]-xmas['x'][0]+1)*(xmas['m'][1]-xmas['m'][0]+1)*(xmas['a'][1]-xmas['a'][0]+1)*(xmas['s'][1]-xmas['s'][0]+1)
curnode = 'in'
q = [curnode]
min_vals = {}
for node in graph.keys():
    min_vals[node] = {'x':[1,4000],'m':[1,4000],'a':[1,4000],'s':[1,4000]}
comb=0
niter = 0
while q:
    curnode = q.pop()
    # print("curnode is", curnode)
    # print("quue", q)
    if curnode in graph.keys():
        prev_range = min_vals[curnode].copy()
        # print("prev range outside loop", prev_range)
        for i in range(len(graph[curnode])): #all except the final default child
            
            child = graph[curnode][i]
            # print("prev range inside loop for child,",child[0], "is", prev_range)
            if len(child) == 1: #no condition = default val
                # print("default node", child)
                if child[0] == 'A': #acceptance
                    comb+= comb_from_range(prev_range)
                elif child[0] != 'R': #some actual node
                    min_vals[child[0]] = prev_range.copy()
                    q.insert(0,child[0])
                    # print("updated child value", min_vals[child[0]])
            else:
                # print("condition node", child)
                in_range, out_range = update_ranges(prev_range[child[1]], child[2], child[3])
                prev_range[child[1]] = in_range
                if child[0] == 'A': #acceptance
                    comb+= comb_from_range(prev_range)
                elif child[0] != 'R': #some actual node
                    min_vals[child[0]] = prev_range.copy()
                    q.insert(0,child[0])
                    # print("updated child value", min_vals[child[0]], "for child", child[0])
                prev_range[child[1]] = out_range
                
    niter+=1

print(comb)