import numpy as np

def get_children(pos,nr,nc,parent=None):
    children=[]
    # if(parent==None):
    if((pos[0]+1)<nr): #down
        children.append([pos[0]+1,pos[1]])
    if((pos[0]-1)>=0): #up
        children.append([pos[0]-1,pos[1]])
    if((pos[1]+1)<nc): #right
        children.append([pos[0],pos[1]+1])
    if((pos[1]-1)>=0): #left
        children.append([pos[0],pos[1]-1])
    # else:
    #     if((pos[0]+1)<nr): #down
    #         if([pos[0]+1,pos[1]]!=parent):
    #             children.append([pos[0]+1,pos[1]])
    #     if((pos[0]-1)>=0): #up
    #         if([pos[0]-1,pos[1]]!=parent):
    #             children.append([pos[0]-1,pos[1]])
    #     if((pos[1]+1)<nc): #right
    #         if([pos[0],pos[1]+1]!=parent):
    #             children.append([pos[0],pos[1]+1])
    #     if((pos[1]-1)>=0): #left
    #         if([pos[0],pos[1]-1]!=parent):
    #             children.append([pos[0],pos[1]-1])
    return children

with open('dec12input.txt') as f:
    x=f.read().strip().split('\n')

st=[0,0]
en=[0,0]
for i,line in enumerate(x):
    j=line.find('S')
    if(j>=0): 
        st[0]=i
        st[1]=j
        break
for i,line in enumerate(x):
    j=line.find('E')
    if(j>=0): 
        en[0]=i
        en[1]=j
        break

zz=[[ch for ch in line] for line in x]
zz[st[0]][st[1]]='a'
zz[en[0]][en[1]]='z'
nr=len(zz)
nc=len(zz[0])
print(nr,nc)
print(st,en)
print(get_children(en,nr,nc,parent=[3,5]))

flag=False
visited=np.zeros((nr,nc),dtype='bool')
visited[:]=False
root=st
visited[root[0],root[1]]=True
queue=[]
queue.append(root)
nsteps=0

while(len(queue)>0):
    mylen=len(queue)
    print("Current queue is", queue)
    while(mylen>0):
        s=queue.pop(0)
        schar=zz[s[0]][s[1]]
        
        print("Popped ",s,"looking at ", schar)
        mychils=get_children(s,nr,nc)
        # print(visited)
        print("Chils are", mychils)
        for chil in mychils:
            print("chil is", chil)
            print("Visit status of chil", visited[chil[0],chil[1]])
            if(visited[chil[0],chil[1]]==False):
                char=zz[chil[0]][chil[1]]
                print("looking at char",char)
                if((ord(char)-ord(schar))<=1):
                    if(chil==en):
                        print("FOUND breaking",nsteps)
                        assert(1==0)
                    print("good chil, adding")
                    visited[chil[0],chil[1]]=True
                    queue.append(chil)
        mylen-=1
    nsteps+=1

print("Total steps",nsteps)

    




