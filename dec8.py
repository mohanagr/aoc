with open('temp.txt') as f:
    x=f.read().strip().split('\n') #temp has temporary testing data

import numpy as np
# print(len(x[0]))
arr = np.zeros((len(x),len(x[0])),dtype='int64')
for i,row in enumerate(x):
    arr[i,:]=np.asarray([a for a in row])
print(arr)
print(arr.shape)
arr2=arr.T #for up-down traversal

# PART 1
# vis = np.zeros(arr.shape,dtype=arr.dtype)
# for i in range(1,arr.shape[0]-1):
#     mymax1=arr[i,0]
#     mymax2=arr[i,-1]
#     mymax3=arr2[i,0]
#     mymax4=arr2[i,-1]
#     for j in range(1,arr.shape[1]-1):
#         if(arr[i,j]>mymax1):
#             vis[i,j]=1
#             mymax1=arr[i,j]
#         if(arr[i,-j-1]>mymax2):
#             vis[i,-j-1]=1
#             mymax2=arr[i,-j-1]
#         if(arr2[i,j]>mymax3):
#             vis[j,i]=1
#             mymax3=arr2[i,j]
#         if(arr2[i,-j-1]>mymax4):
#             vis[-j-1,i]=1
#             mymax4=arr2[i,-j-1]

right = np.ones(arr.shape,dtype=arr.dtype)
left  = right.copy()
down = right.copy()
up = right.copy()

for i in range(1,arr.shape[0]-1):
    yy1=1
    yy2=-2
    yy3=1
    yy4=-2
    mymax1=arr[i,yy1]
    mymax2=arr[i,yy2]
    mymax3=arr2[i,yy3]
    mymax4=arr2[i,yy4]
    for j in range(2,arr.shape[1]-1):
        if(arr[i,j]<mymax1):
            right[i,yy1]+=1
        else:
            yy1=j
            mymax1=arr[i,j]
        if(arr[i,-j-1]<mymax2):
            left[i,yy2]+=1
        else:
            yy2=-j-1
            mymax2=arr[i,-j-1]

        # #right is down for transpose
        if(arr2[i,j]<mymax3):
            down[yy3,i]+=1
        else:
            yy3=j
            mymax3=arr2[i,j]
        if(arr2[i,-j-1]<mymax4):
            up[yy4,i]+=1
        else:
            yy4=-j-1
            mymax4=arr2[i,-j-1]
        
print("left\n",left)
print("right\n",right)
print("up\n",up)
print("down\n",down)

print(left*right*up*down)     
print(np.max(left*right*up*down))







    
