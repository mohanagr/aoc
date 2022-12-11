with open('dec8input.txt') as f:
    x=f.read().strip().split('\n') #temp has temporary testing data

import numpy as np

for _ in range(4):
    for x,y in np.ndindex(grid.shape):
        # print(x,y)   
        lower = [t < grid[x,y] for t in grid[x,y+1:]]

        part1[x,y] |= all(lower)
        part2[x,y] *= next((i+1 for i,t in enumerate(lower) if ~t), len(lower))

    grid, part1, part2 = map(np.rot90, [grid, part1, part2])


# print(arr)
# print(arr.shape)
arr2=arr.T #for up-down traversal

# # PART 1
# # vis = np.zeros(arr.shape,dtype=arr.dtype)
# # for i in range(1,arr.shape[0]-1):
# #     mymax1=arr[i,0]
# #     mymax2=arr[i,-1]
# #     mymax3=arr2[i,0]
# #     mymax4=arr2[i,-1]
# #     for j in range(1,arr.shape[1]-1):
# #         if(arr[i,j]>mymax1):
# #             vis[i,j]=1
# #             mymax1=arr[i,j]
# #         if(arr[i,-j-1]>mymax2):
# #             vis[i,-j-1]=1
# #             mymax2=arr[i,-j-1]
# #         if(arr2[i,j]>mymax3):
# #             vis[j,i]=1
# #             mymax3=arr2[i,j]
# #         if(arr2[i,-j-1]>mymax4):
# #             vis[-j-1,i]=1
# #             mymax4=arr2[i,-j-1]

right = np.ones(arr.shape,dtype=arr.dtype)
left  = right.copy()
down = right.copy()
up = right.copy()
print(arr)
import itertools
for i in range(1,arr.shape[0]-1):
    for j in range(1,arr.shape[1]-1):
        # print("EXAMINING:", i, j)
        ii=arr[i,j]
        jj=arr2[i,j]
        right[i,j]+= len(list(itertools.takewhile(lambda x:x<ii,arr[i,j+1:-1])))
        left[i,j]+= len(list(itertools.takewhile(lambda x:x<ii,arr[i,j-arr.shape[1]-1:-arr.shape[1]:-1])))
        down[j,i]+= len(list(itertools.takewhile(lambda x:x<jj,arr2[i,j+1:-1])))
        up[j,i]+= len(list(itertools.takewhile(lambda x:x<jj,arr2[i,j-arr.shape[0]-1:-arr.shape[0]:-1])))
        
# print(arr)
# print("left\n",left)
# print("right\n",right)  
# print("up\n",up)
# print("down\n",down)

print("MY ANSWER--------------------------")
print(left*right*up*down)     
print(np.max(left*right*up*down))







    
