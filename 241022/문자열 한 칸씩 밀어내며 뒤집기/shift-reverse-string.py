strs, q = list(input().split())
# strs = list(strs)
q = int(q)

for i in range(q):
    quest = int(input())
    
    if quest == 1:
        strs = strs[1:] + strs[0]
    elif quest == 2:
        strs = strs[-1] + strs[:-1]
    else:
        strs = strs[::-1]
    
    print(strs)