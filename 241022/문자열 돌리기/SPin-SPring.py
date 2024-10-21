strs = input()

L = len(strs)

print(strs)

for i in range(L):
    strs = strs[-1] + strs[:-1]
    print(strs)