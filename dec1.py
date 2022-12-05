# elftot=0
# cals = []
# with open('dec1input.txt') as f:
#     lines=f.readlines()
# for l in lines:
#     if(l=='\n'):
#         # print(elftot)
#         cals.append(elftot)
#         elftot=0
#     else:
#         elftot+=int(l.strip())
# cals.append(elftot)

with open('dec1input.txt') as f:
    x=f.read().strip().split('\n\n')
cals=[sum(map(int, a.split('\n'))) for a in x]

cals.sort()
print(sum(cals[-3:]))


