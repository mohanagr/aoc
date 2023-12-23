import numpy as np

def draw(crt):
    for i in range(0,6):
        print(crt[i*40:(i+1)*40])

with open('dec10input.txt') as f:
    x=f.read().strip().split('\n')
# print(x)
# x=x[:500]
steps=[]
reg=1
for val in x:

    a=val.split(' ')
    if(a[0]=='noop'):
        steps.append(reg)
        continue
    steps.extend(2*[reg])
    reg+=int(a[1])

s=0 # part 1
for i in range(0,6):
    cyc=(20+i*40)
    s+=cyc*steps[cyc-1]

crt = len(steps)*['.']

for i in range(0,len(steps)): #CRT positions in each cycle
    # print("cycle", i+1, "reg val during cyc", steps[i])
    crtpos = i%40
    # print("Current CRT", crt[:i+1])
    if((crtpos>=steps[i]-1)and(crtpos<=steps[i]+1)):
        # print("CRT at cyc", i+1, "is #")
        crt[i]='#'

crt=''.join(crt)
draw(crt)

