# from collections import deque
import sys
def bigmult(a,b):
    # print("Multiplying", a, b)
    result = [0] * (len(a)+len(b))
    for idx,m in enumerate(a[::-1]):
        # print("m is", m)
        carry=0
        temp = [0] * len(result)
        ii=idx
        for n in b[::-1]:
            c = int(n)*int(m) + carry
            # print("C is ", c)
            temp[ii]=c%10
            carry=c//10
            ii+=1
        temp[ii]=carry
        # print("temp",temp)
        carry=0
        ii=0
        while(ii<len(result)):
            # print("adding", result[ii],temp[ii],carry)
            s = result[ii]+temp[ii]+carry
            carry=s//10
            result[ii]=s%10
            # print("s is",s)
            ii+=1
        # print("result after one loop", result)
    # print("Result of mult is", ''.join(str(a) for a in result[ii::-1]))
    return ''.join(str(a) for a in result[ii::-1])
def bigmod(x,a):
    # print("Modding", x, a)
    b=10%a
    res=0
    for dig in x:
        res = (res*10 + int(dig)%a)%a
    # print("result of mod is", res)
    return res
def bigadd(temp2,temp1):
    # print("Adding", temp2, temp1)
    carry2=0
    result=[0]*(max(len(temp2),len(temp1))+1)
    i=0
    while(i<min(len(temp1),len(temp2))):
        s = int(temp2[-i-1])+int(temp1[-i-1])+carry2
        carry2=s//10
        result[i]=s%10
        i+=1
    while(i<len(temp1)):
        s = int(temp1[-i-1])+carry2
        carry2=s//10
        result[i]=s%10
        i+=1
    while(i<len(temp2)):
        s = int(temp2[-i-1])+carry2
        carry2=s//10
        result[i]=s%10
        i+=1
    result[i] = carry2
    return ''.join(str(x) for x in result[i::-1])

class Monkey:
    def __init__(self,items,opfunc,div,testtrue,testfalse,friends=None):
        # self.items=items
        self.items=items
        # print(self.items)
        self.lcm=None
        self.ninspect=0
        self.inspect=opfunc
        self.friends=friends
        self.div=div
        self.testtrue=testtrue
        self.testfalse=testfalse
    def test(self,item):
        if(item%self.div==0):
            self.friends[self.testtrue].items.append(item)
        else:
            self.friends[self.testfalse].items.append(item)
    def inspectAll(self):
        for item in self.items:
            self.ninspect+=1
            item=self.inspect(item)%self.lcm
            self.test(item)
        self.items=[]
    def initItems(self):
        if(self.friends):
            self.lcm = 1
            for x in self.friends:
                self.lcm*=x.div
            self.items = [y%self.lcm for y in self.items]

        # self.ninspect+=len(self.items)
        # for x in map(self.inspect,self.items):
        #     # print(x,"\n", type(x))
        #     # if(len(x)>1000): 
        #     #     print("ABORT!")
        #     #     sys.exit(1)
        #     self.test(x)
        # self.items=[]
    

monkeys=[]
# monkeys.append(Monkey([79, 98],lambda x:x*19,23,2,3))
# monkeys.append(Monkey([54, 65, 75, 74],lambda x:x+6,19,2,0))
# monkeys.append(Monkey([79, 60, 97],lambda x:x*x,13,1,3))
# monkeys.append(Monkey([74],lambda x:x+3,17,0,1))

# monkeys.append(Monkey([79, 98],lambda x:bigmult(x,'19'),23,2,3))
# monkeys.append(Monkey([54, 65, 75, 74],lambda x:bigadd(x,'6'),19,2,0))
# monkeys.append(Monkey([79, 60, 97],lambda x:bigmult(x,x),13,1,3))
# monkeys.append(Monkey([74],lambda x:bigadd(x,'3'),17,0,1))


monkeys.append(Monkey([52, 78, 79, 63, 51, 94],lambda x:x*13,5,1,6))
monkeys.append(Monkey([77, 94, 70, 83, 53],lambda x:x+3,7,5,3))
monkeys.append(Monkey([98, 50, 76],lambda x:x*x,13,0,6))
monkeys.append(Monkey([92, 91, 61, 75, 99, 63, 84, 69],lambda x:x+5,11,5,7))
monkeys.append(Monkey([51, 53, 83, 52],lambda x:x+7,3,2,0))
monkeys.append(Monkey([76, 76],lambda x:x+4,2,4,7))
monkeys.append(Monkey([75, 59, 93, 69, 76, 96, 65],lambda x:x*19,17,1,3))
monkeys.append(Monkey([89],lambda x:x+2,19,2,4))
for m in monkeys:
    m.friends=monkeys
    m.initItems()
import time

t1=time.time()
for i in range(0,10000):
    for j,m in enumerate(monkeys[:]):
        # print(f"Monkey {j}....")
        m.inspectAll()
    if((i+1)%100==0):
        print("After Round", i+1)
        for i,m in enumerate(monkeys):
            print(f"Monkey {i}:", m.ninspect)
t2=time.time()
print((t2-t1)/100, "avg time per round")

monkeybiz=sorted([m.ninspect for m in monkeys],reverse=True)
print(monkeybiz)
print(monkeybiz[0]*monkeybiz[1])







