def myscore(mystr):
    elf,me = mystr.split(' ')
    s=0
    score = {'rock':1,'paper':2,'scissor':3}
    rock=['A','X']
    paper=['B', 'Y']
    scissor=['C','Z']
    if(elf in rock):
        if(me in rock):
            s=score['rock']+3
        elif(me in paper):
            s=score['paper']+6
        else:
            s=score['scissor']
    elif(elf in paper):
        if(me in paper):
            s=score['paper']+3
        elif(me in scissor):
            s=score['scissor']+6
        else:
            s=score['rock']
    elif(elf in scissor):
        if(me in scissor):
            s=score['scissor']+3
        elif(me in rock):
            s=score['rock']+6
        else:
            s=score['paper']
    return s

def myscore2(mystr):
    elf,res = mystr.split(' ')
    s=0
    score = {'rock':1,'paper':2,'scissor':3}

    rock=['A']
    paper=['B']
    scissor=['C']

    if(res=='X'):
        #lose
        if(elf in rock):
            s=score['scissor']
        elif(elf in paper):
            s=score['rock']
        else:
            s=score['paper']
    elif(res=='Y'):
        #draw
            if(elf in rock):
                s=score['rock']+3
            elif(elf in paper):
                s=score['paper']+3
            else:
                s=score['scissor']+3
    elif(res=='Z'):
        #win
        if(elf in rock):
            s=score['paper']+6
        elif(elf in paper):
            s=score['scissor']+6
        else:
            s=score['rock']+6
    return s
    
    


with open('dec2input.txt') as f:
    x=f.read().strip().split('\n')
# print(x)
cals=sum((map(myscore2,x)))

print(cals)
# print(cals)