import collections
from functools import cmp_to_key
def score_hand(c1):
    #remove all J from counter
    num_J = c1['J']
    del c1['J']
    if len(c1)==0:
        return 7 # was all J's, so five of a kind
    new_max= max(c1.values()) + num_J
    # print(c1)
    if len(c1.keys())==1:
        #five of a kind
        score_c1 = 7
    elif len(c1.keys())==2:
        #four of a kind or full house
        if min(c1.values())==1:
            #four of a kind
            score_c1 = 6
        else:
            score_c1 = 5
    elif len(c1.keys())==3:
        #two pair or three of a kind
        if new_max==3:
            #three of a kind
            score_c1 = 4
        else:
            score_c1 = 3
    elif len(c1.keys())== 4:
        # one pair
        score_c1 = 2
    else:
        #high card
        score_c1 = 1
    return score_c1

# x = '2,3,4,5,6,7,8,9,T,J,Q,K,A'
x = 'J,2,3,4,5,6,7,8,9,T,Q,K,A'
mymap={}
for i,char in enumerate(x.split(',')):
    mymap[char]=i

def mysort(a,b):
    c1=collections.Counter(a)
    c2=collections.Counter(b)
    score_c1 = score_hand(c1)
    score_c2 = score_hand(c2)
    if score_c1 > score_c2:
        return 1
    elif score_c1 < score_c2:
        return -1
    else:
        #both hands equal. check high card
        for i in range(5):
            if mymap[a[i]] > mymap[b[i]]:
                return 1
            elif mymap[a[i]] < mymap[b[i]]:
                return -1
        return 0

with open('dec7.txt') as f:
    lines=f.read().strip().split('\n')

hands_dict = {line.split()[0]:line.split()[1] for line in lines}

new_hands = sorted(hands_dict.keys(),key=cmp_to_key(mysort))

score = sum([(i+1)*int(hands_dict[new_hands[i]]) for i in range(len(new_hands))])
print(score)
