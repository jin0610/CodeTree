strs = input()

L = len(strs)

for i in range(L):
    print(strs[-i:] + strs[:-i])
print(strs)