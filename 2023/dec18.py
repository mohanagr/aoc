with open('dec18.txt') as f:
    lines=f.read().strip().split('\n')
import numpy as np
xy = np.zeros((len(lines)+1,2),dtype=int)
xy[0,0]=0
xy[0,1]=0
boundary=[]
row=0
col=0
newrow=row
newcol=col
blen=0
# mymap = np.zeros((1000,1000),dtype=int)
for i,line in enumerate(lines):
    dirn,size,color = line.split(' ')
    size = int(color[2:7],16)
    dirn = int(color[7],16)
    print(size,dirn)
    if dirn == 0:
        newcol = col + int(size)
    elif dirn == 2:
        newcol =  col - int(size)
    elif dirn == 3:
        newrow = row -  int(size)
    elif dirn == 1:
        newrow = row + int(size)
    # if np.abs(newcol) > maxc:
    #     maxc = np.abs(newcol)
    # if np.abs(newrow) > maxr:
    #     maxr = np.abs(newrow)

    boundary.append(str(row)+'_'+str(col))
    blen+=int(size)
    # if newcol <0 or newrow <0:
    #     print("SHIT", newcol,newrow)
    #     exit(1)
    # print("going to", newrow, newcol)
    # if(col>newcol):
    #     mymap[row:newrow+1, newcol:col+1]=1
    # elif(row>newrow):
    #     mymap[newrow:row+1, col:newcol+1]=1
    # else:
    #     mymap[row:newrow+1, col:newcol+1]=1
    row = newrow
    col = newcol
    xy[i+1,0]=col
    xy[i+1,1]=row
# print("maxrow maxc", maxr,maxc)

print("total len", blen)
# print("boundary is", boundary)
d=15
np.set_printoptions(threshold=1000000)
# print(xy)
area = 0.5*np.sum(xy[:-1,0]*xy[1:,1] - xy[1:,0]*xy[:-1,1]) #green's theorem or shoelace formula
inside = (area- blen/2 + 1) #picks theorem
# print(blen,inside)
print("total vol", blen+inside)
