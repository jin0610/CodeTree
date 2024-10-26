n = int(input())

arr = [0] * 202
idx = 100
for i in range(n):
    x, d = input().split()
    x = int(x)

    if d == "R":
        for j in range(idx+1, idx + x+1):
            arr[j] += 1
        idx = idx + x
    else:
        for j in range(idx-1, idx-x-1, -1):
            arr[j] += 1
        idx = idx - x
   

cnt = 0
for i in arr:
    if i >= 2:
        cnt += 1

print(cnt)