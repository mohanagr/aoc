with open('dec4input.txt') as f:
    x=f.read().strip().split('\n')


print("Part1",sum(map(lambda elfs: 1 if((elfs[0][0]<=elfs[1][0] and elfs[0][1]>=elfs[1][1]) or (elfs[0][0]>=elfs[1][0] and elfs[0][1]<=elfs[1][1])) else 0,[[list(map(int,e.split('-'))) for e in line.strip().split(",")] for line in x])))
print("Part1",sum(map(lambda elfs: 1 if((elfs[0][0]<=elfs[1][0] and elfs[0][1]>=elfs[1][1]) or (elfs[0][0]>=elfs[1][0] and elfs[0][1]<=elfs[1][1])) else 0,[[list(map(int,e.split('-'))) for e in line.strip().split(",")] for line in x])))
d=[line.strip().split(",") for line in x]
for pair in d:
    # print(l)
    elf1 = [int(i) for i in pair[0].split("-")]
    elf2 = [int(i) for i in pair[1].split("-")]
    if((elf1[0]<=elf2[0] and elf1[1]>=elf2[1]) or (elf1[0]>=elf2[0] and elf1[1]<=elf2[1])):
        s+=1
    # elif(elf1[0]>=elf2[0] and elf1[1]<=elf2[1]):
    #     s+=1
    # if(elf1[0]<=elf2[1] and elf2[0]<=elf1[0]): #elf1 poora elf2 ke andar in this
    #     s1+=1
    # elif(elf2[0]<=elf1[1] and elf1[0]<=elf2[0]): #elf2 poora elf1 ke andar in this
    #     s1+=1
print(s,s1)
