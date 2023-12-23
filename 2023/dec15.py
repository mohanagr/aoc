with open('dec15.txt') as f:
    cmds=f.read().strip().split(',')

def hash(mystr):
    val=0
    for char in list(mystr):
        val+=ord(char)
        val*=17
        val%=256
    return val

def get_index(label,arr):
    for i,a in enumerate(arr):
        if a[0]==label:
            return i
    return None

boxes={}
s=0
for c in cmds:
    # print("processing", c)
    if '-' in c:
        label=c.split('-')[0]
        # print(label)
        boxnum = hash(label)
        # print("boxnum for ", label, "is ", boxnum)
        if boxnum not in boxes.keys():
            print("trying to remove something in a box that doesn't exist")
            continue
            # boxes[boxnum]=[]
        lens_id = get_index(label,boxes[boxnum])
        if lens_id is not None:
            del boxes[boxnum][lens_id]
        else:
            # print("trying to remove something that dont exist")
            pass
    else: #add or update a lens
        aa=c.split('=')
        label,power=aa
        # print(label,power)
        boxnum = hash(label)
        if boxnum not in boxes.keys():
            boxes[boxnum]=[]
        lens_id = get_index(label,boxes[boxnum])
        if lens_id is not None:
            boxes[boxnum][lens_id]=[label,power] #update
        else:
            boxes[boxnum].append([label,power])
sbig=0
for boxnum in boxes.keys():
    if len(boxes[boxnum])>0: #lenses exist
        for lensnum in range(len(boxes[boxnum])):
            s=(1+boxnum)*(lensnum+1)*int(boxes[boxnum][lensnum][1])
            # print(s)
            sbig+=s
print(sbig)

