with open('dec6input.txt') as f:
    x=f.read().strip().split('\n')[0]
L=14
for i in range(len(x)-L-1):
    if(len(set(x[i:i+L]))==L):
        print("GOT", i+L)
        break

# non-set solution
for i in range(len(x)-13):
    flag=1
    substr = x[i:i+14]
    substr=sorted(substr)
    for j in range(len(substr)-1):
        if(substr[j]==substr[j+1]):
            flag=0
            break
    if(flag):
        print(substr, "GOT IT", i+14)
        break




    