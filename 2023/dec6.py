with open('dec6.txt') as f:
    lines=f.read().strip().split('\n')
import re
import math
myre = re.compile(r"\d+")
times=myre.findall(lines[0])
rec=myre.findall(lines[1])
print(times,rec)
prod=1
for i in range(len(times)):
    T=int(times[i])
    d=int(rec[i])
    det=math.sqrt(T**2-4*d)
    x=math.ceil((T-det)/2)
    y=math.floor((T+det)/2)
    prod*=(y-x+1)
print(prod)