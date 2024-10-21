strs=[]
for i in range(10):
    strs.append(input())

s = input()

for idx in strs:
    if(idx[-1] == s):
        print(idx)