with open('dec4.txt') as f:
    lines=f.read().strip().split('\n')
import re
myre = re.compile(r"\d+")
card_copies = np.ones(len(lines))

s=0
for i,line in enumerate(lines):
    wins,haves = map(myre.findall, [x.strip() for x in line.split(":")[1].split("|")])
    mydict = {}
    found=[]
    #O(n) soln
    for win in wins:
        mydict[win]=True
    for have in haves:
        try:
            mydict[have]
            found.append(have)
        except KeyError:
            pass
    matches = len(found)
    #s+=matches
    # print(matches)
    card_copies[i+1:i+matches+1] += card_copies[i]  

print(np.sum(card_copies))


