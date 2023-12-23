with open('dec5.txt') as f:
    lines=f.read().strip().split('\n\n')

def get_dest(src, mapping):
    for m in mapping:
        dest_start,src_start,dist=[int(x) for x in m.split(' ')]
        if(src >= src_start and src < src_start + dist):
            src = dest_start + src - src_start
            break
    return src

import re

def check_block(block,Range1,Range2,chunkz_mapped, chunkz_mapping):
    # mapped is to keep track of what bits of block accounted for by the provided mapping
    # mapping contains the said mapping. and then we need to add unaccounted parts of the block which map to themselves
    s0,e0 = block
    s1,e1 = Range1 #mapped from
    s11,e11=Range2 #mapped to
    if(e1>=s0):
        if(s1>=s0):
            if(s1<=e0):
                if(e1>e0):
                    #print(s1,e0)
                    chunkz_mapped[s1]=e0
                    chunkz_mapping[s11]=s11+e0-s1
                else:
                    #print(s1,e1)
                    chunkz_mapped[s1]=e1
                    chunkz_mapping[s11]=e11
        else:
            if(e1>=e0):
                #print(s0,e0)
                chunkz_mapped[s0]=e0
                chunkz_mapping[s11+s0-s1]=s11+e0-s1
            else:
                #print(s0,e1)
                chunkz_mapped[s0]=e1
                chunkz_mapping[s11+s0-s1]=e11
    # return chunkz

def add_missed_chunkz(block, chunkz_mapped, chunkz_mapping):
    keys = sorted(list(chunkz_mapped.keys()))
    
    keys.append(block[1]+1) #add end value
    end = block[0]-1
    # print(keys[0]-1, end)
    # print("keys are", keys)
    for key in keys:
        # print("cur key", key)
        if key-1 != end:
            # print(key-1,end,"cmp")
            # print(end+1,key-1)
            # print('am here')
            chunkz_mapping[end+1] = key-1
        try:
            end = chunkz_mapped[key]
        except:
            pass

#tree based BFS solution for part2

re_num = re.compile("\d+")
seednums = re_num.findall(lines[0])
# loc_nums = []
# # print(seednums)
# # for seed in seednums:
# #     start =  int(seed)
# #     for catg in lines[1:]:
# #         line_tags = catg.split("\n")
# #         start = get_dest(start,line_tags[1:])
# #     loc_nums.append(start)
# #     # print(f"seednum: {seed}, location: {start}")
# # print(min(loc_nums))
start_id = []
seednums=[int(seed) for seed in seednums]
for i in range(0,len(seednums),2):
    # if(i>0): break
    seedrange = [seednums[i], seednums[i]+seednums[i+1]-1]
    block=seedrange
    # root = TreeNode(seedrange)
    # print(seedrange)
    curnodes = [seedrange]
    for myiter, catg in enumerate(lines[1:]):
        # print("myiter is ", myiter)
        # if(myiter>3): break
        newnodes = []
        values = catg.split("\n")
        while len(curnodes)>0:
            block = curnodes.pop()
            chunkz_mapped={}
            chunkz_mapping={}
            for val in values[1:]:
                dest_start, src_start, dist = [int(x) for x in val.split()]
                # print("vals are", dest_start, src_start, dist)
                check_block(block,[src_start,src_start+dist],[dest_start,dest_start+dist],chunkz_mapped, chunkz_mapping)
                # print(chunkz_mapped)
            add_missed_chunkz(block,chunkz_mapped, chunkz_mapping)
            # print(chunkz_mapped, chunkz_mapping)
            for key in chunkz_mapping.keys():
                newnodes.append([key,chunkz_mapping[key]])
        curnodes = newnodes
    for n in newnodes:
        start_id.append(n[0])
    # start = get_dest(start,line_tags[1:])
    # loc_nums.append(start)
    # print(f"seednum: {seed}, location: {start}")
print(min(start_id))



