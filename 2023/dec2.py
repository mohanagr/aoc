import re
with open('dec2.txt') as f:
    lines=f.read().strip().split('\n')

obj=re.compile(r"(\d{1,2})(?=\s(red|blue|green))")
valid_games = []
mymap={'red':12,
'green':13,
'blue':14}
s=0
for ID,l in enumerate(lines):
    matches=obj.finditer(l)
    flag=1
    maxdict={'red':0,'blue':0,'green':0} #part 2
    # for m in matches: #part1
    #     if int(m.group(1)) > mymap[m.group(2)]:
    #         flag=0
    #         break
    # if(flag):
    #     valid_games.append(ID+1)
    for m in matches:
        if int(m.group(1)) > maxdict[m.group(2)]:
            maxdict[m.group(2)] = int(m.group(1))
    # print(maxdict)
    s += maxdict['red'] * maxdict['green'] * maxdict['blue']
    if(maxdict['red'] * maxdict['green'] * maxdict['blue'] ==0):
        print("crazy shit in game #", ID+1)
# print(sum(valid_games))
print(s)

