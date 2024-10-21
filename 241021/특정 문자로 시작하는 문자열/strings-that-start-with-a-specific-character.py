n = int(input())
strs=[]
for i in range(n):
    strs.append(input())
s = input()

length = 0
cnt = 0

for str in strs:
    if(str[0] == s):
        length = length + len(str)
        cnt += 1

print(cnt, "%.2f"%(length/cnt))