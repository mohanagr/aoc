import re
import numpy as np

def get_neigbour_sum(row, cst,cen, nrows, ncols, flags):
    r1 = row-1
    r2 = row+2
    c1 = cst-1
    c2 = cen+1
    # print(r1,r2,c1,c2)
    if(row-1 < 0):
        r1 = row
    if(c1 < 0):
        c1 = cst
    if(r2 > nrows):
        r2 = nrows
    if(c2 > ncols):
        c2 = ncols
    # print(r1,r2,c1,c2)
    return np.sum(flags[r1:r2,c1:c2])

def get_stars(row, cst,cen, nrows, ncols, flags, gearnum):
    r1 = row-1
    r2 = row+2
    c1 = cst-1
    c2 = cen+1
    # print(r1,r2,c1,c2)
    if(row-1 < 0):
        r1 = row
    if(c1 < 0):
        c1 = cst
    if(r2 > nrows):
        r2 = nrows
    if(c2 > ncols):
        c2 = ncols
    # print(r1,r2,c1,c2)
    s = np.sum(flags[r1:r2,c1:c2])
    if(s>0):
        rows,cols=np.where(flags[r1:r2,c1:c2]==True)
        rows+=r1
        cols+=c1
        return [str(a)+"_"+str(b) for a,b in zip(rows,cols)]
    return None


with open('dec3.txt') as f:
    lines=f.read().strip().split('\n')

a = np.zeros((len(lines), len(lines[0])), dtype='bool')

# myre = re.compile(r"[^\d.]")
myre = re.compile(r"\*")
starIDs = {}

for i,line in enumerate(lines):
    matches = myre.finditer(line)
    # print("line", i, list(matches))
    for match in matches:
        row = i
        col = match.start()
        a[row,col]=True
        starIDs[str(row)+"_"+str(col)] = []
        # adj = [lines[row-1][col], lines[row+1][col], lines[row][col+1], lines[row][col-1],\
        # lines[row-1][col-1], lines[row-1][col+1], lines[row+1][col-1], lines[row+1][col+1] ]
        # print(adj)
# print(a)
# print(starIDs)
# myre = re.compile(r"\d+")
# mysum=0
# for i,line in enumerate(lines):
#     matches = myre.finditer(line)
#     # print("line", i, list(matches))
#     for match in matches:
#         row = i
#         col = match.start()
#         dec = get_neigbour_sum(row,match.start(),match.end(),a.shape[0],a.shape[1], a)
#         if(dec==1):
#             mysum+=int(line[match.start():match.end()])
# # print(a.astype(int))
# print(mysum)

myre = re.compile(r"\d+")
mysum=0
for i,line in enumerate(lines):
    matches = myre.finditer(line)
    # print("line", i, list(matches))
    for match in matches:
        row = i
        col = match.start()
        gearnum = int(line[match.start():match.end()])
        keys = get_stars(row,match.start(),match.end(),a.shape[0],a.shape[1], a,gearnum)
        if(keys):
            for key in keys:
                starIDs[key].append(gearnum)
sss=0
for key in starIDs.keys():
    if(len(starIDs[key])==2):
        # print(starIDs[key][0]*starIDs[key][1])
        sss+=starIDs[key][0]*starIDs[key][1]

# print(starIDs)
# print(a.astype(int))
# print(mysum)
print(sss)