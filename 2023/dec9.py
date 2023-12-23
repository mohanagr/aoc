with open('dec9.txt') as f:
    lines=f.read().strip().split('\n')

import re
import numpy as np

def get_val(arr):
    if np.sum(arr)==0:
        return 0
    # return arr[-1] + get_val(np.diff(arr)) #part 1
    return arr[0] - get_val(np.diff(arr)) #part 2

s=0
for line in lines:
    arr = [int(b) for b in line.split()]
    # print(arr)
    # print(np.diff(arr))
    # print(get_val(arr))
    s+=get_val(arr)
print(s)
    