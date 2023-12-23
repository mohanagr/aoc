import re

with open('dec1.txt') as f:
    x=f.read().strip().split('\n')

reobj = re.compile(r"(\d)|(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)")
mymap={"one":'1',"two":'2',"three":'3',"four":'4',"five":'5',"six":'6',"seven":'7',"eight":'8',"nine":'9'}
s=0
for l in x:
    # print(l)
    a=re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))",l)
    start=a[0]
    end=a[-1]
    if(len(start)>1):
        start=mymap[start]
    if(len(end)>1):
        end=mymap[end]
    # print(start,end)
    # print(int(a[0]+a[-1]))
    s+=int(start+end)
print(s)