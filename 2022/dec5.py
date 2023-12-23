with open('dec5input.txt') as f:
    x=f.read().split('\n\n')

a=x[0].split('\n')
# print(a)
ncols = (len(a[0])+1)//4
nrows = len(a)-1
stacks = []
print(nrows,ncols)
for i in range(ncols):
    temp=[]
    for j in range(nrows):
        # print("row", j, a[j])
        # print("Accessing str col", ncols*i+1+i, "for", ncols, i, j)
        myletter=a[nrows-j-1][3*i+1+i]
        # print("myletter", myletter)
        if(ord(myletter)<=90 and ord(myletter)>=65):
            # print("appending")
            temp.append(myletter)
    stacks.append(temp)
print(stacks)

moves=x[1].split('\n')

# print(moves)


for move in moves:
    zz=move.split(' ')
    print(zz)
    npops = int(zz[1])
    i = int(zz[3])
    j = int(zz[5])
    # print(npops,i,j)
    tempstack=[]
    for pop in range(npops):
        tempstack.append(stacks[i-1].pop())
        # stacks[j-1].append(stacks[i-1].pop())
    for i in range(len(tempstack)):
        stacks[j-1].append(tempstack.pop())
    
    print("After move", stacks)

l=[]
for stack in stacks:
    l.append(stack[-1])
print(''.join(l))


