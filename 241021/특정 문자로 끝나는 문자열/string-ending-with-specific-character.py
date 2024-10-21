strs=[]
for i in range(10):
    strs.append(input())

s = input()

cnt = 0
for idx in strs:
    if(idx[-1] == s):
        print(idx)
        cnt += 1
if(cnt == 0):
    print("None")