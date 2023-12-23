with open('dec12.txt') as f:
    lines=f.read().strip().split('\n')

import functools
# def get_combo(mystr,targets):
#     count = 0
#     i = 0
#     j = 0
#     # print("string is ", ''.join(mystr))
#     while(i < len(mystr)):
#         char = mystr[i]
#         # print('current char', char)
#         if char == '.':
#             # print("check count", count)
#             if j < len(targets) and count > 0: #if count = 0, it's possible we haven't encountered # yet.
#                 if count == targets[j]:
#                     j += 1
#                     count = 0
#                 else:
#                     # print("wrong num of # found")
#                     return 0 # wrong num of # found
#             else:
#                 if count > 0: #all targets reached but more # found
#                     # print("all targets reached but more # found")
#                     return 0
#         elif char == '#':
#             # print("incr count")
#             count += 1
#         elif char == '?':
#             mystr[i] = '.'
#             result1 = get_combo(mystr.copy(),targets)
#             mystr[i] = '#'
#             result2 = get_combo(mystr.copy(),targets)
#             return result1 + result2
#         # print("continuing")
#         i += 1
#     if j < len(targets): # string ends with #'s *** possible bug here
#         if count == targets[j]:
#             # print("str ends with # and count matches target")
#             j += 1
#             count = 0
#         else: 
#             # print("str ends with # and count doesnt match target")
#             return 0
#     else:
#         if count > 0: #all targets reached but more # found
#             return 0
#     if j < len(targets): # all targets not reached
#         #we ran out of string but targets remain, not viable
#         return 0
#     return 1

#try to write this without a loop. might allow memoization.
global mystr,targets

@functools.lru_cache(maxsize=None)
def get_combo(i,j,count):
    global mystr,targets
    # print("string is ", ''.join(mystr))
    # print("params:", i, j, count)
    
    def dot():
    # print("check count", count)
        if j < len(targets):
            if count > 0: #if count = 0, it's possible we haven't encountered # yet.
                if count == targets[j]:
                    return get_combo(i+1,j+1,0)
                else:
                    # print("wrong num of # found")
                    return 0 # wrong num of # found
        else:
            if count > 0: #all targets reached but more # found
                # print("all targets reached but more # found")
                return 0
        retval = get_combo(i+1,j,count)
        return retval
        # print("ret val is ", retval)
            
    def pound():
            return get_combo(i+1,j,count+1)
        
    if i < len(mystr):
        char = mystr[i]
        # print('current char', char)
        if char == '.': return dot()
        elif char == '#': return pound()
        elif char == '?':
            return dot() + pound()
        # print("continuing")
    else:
        
        if j < len(targets): # string ends with #'s *** possible bug here
            if count == targets[j]:
                # print("str ends with # and count matches target")
                j += 1
                count = 0
            else: 
                # print("am here returning 0")
                # print("str ends with # and count doesnt match target")
                return 0
        else:
            if count > 0: #all targets reached but more # found
                return 0
        if j < len(targets): # all targets not reached
            #we ran out of string but targets remain, not viable
            return 0
        return 1


s = 0
mult=5
for line in lines:
    mystr, targets = line.split(' ')
    targets = [int(x) for x in targets.split(',')]
    mystr = '?'.join([mystr]*mult)
    # print(mystr)
    targets = targets*mult
    ss = get_combo(0,0,0)
    s+=ss
    get_combo.cache_clear()
    print(mystr,targets, ss)
print("tot sum", s)