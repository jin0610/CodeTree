strs = list(input())

s = strs[1]
for i in range(len(strs)):
    if(strs[i] == s):
        strs[i] = strs[0]

print(''.join(strs))