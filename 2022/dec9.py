import numpy as np

with open('dec9input.txt') as f:
    x=f.read().strip().split('\n')
# print(x)
# x=x[:500]
steps=[]
for val in x:
    # print (val)
    key,num=val.split(' ')
    # print(key, num)
    steps.extend(int(num)*[key])

# print(steps)
pos = []

def update(Hx,Hy,Tx,Ty):
    dx = Hx-Tx
    dy = Hy-Ty
    # print("dx dy", dx, dy)
    if(np.abs(dx)>1 or np.abs(dy)>1):
        # print("updating")
        Tx+=np.sign(dx)
        Ty+=np.sign(dy)
    return Tx,Ty
    
Hx,Hy=[0,0]
Tails=[] # only 1 tail for part 1
for i in range(0,9):
    Tails.append([0,0])

print(Tails)
for step in steps:
    # print("Taking step:", step)
    if(step=='R'):
        Hx+=1
    elif(step=='L'):
        Hx-=1
    elif(step=='U'):
        Hy+=1
    elif(step=='D'):
        Hy-=1
    # print("New Hx, Hy", Hx, Hy)
    Tails[0] = update(Hx,Hy,Tails[0][0],Tails[0][1])
    for i in range(1,len(Tails)):
        Tails[i] = update(Tails[i-1][0],Tails[i-1][1],Tails[i][0],Tails[i][1])
    # Tx,Ty=update(Hx,Hy,Tx,Ty)
    # print("New Tx, Ty", Tx, Ty)
    # pos[str(Tx)+str(Ty)]=1
    # pos.append((Tx,Ty))
    pos.append((Tails[-1][0],Tails[-1][1]))


# print(pos.keys())
# print(len(pos.keys()))
print(len(set(pos)))

