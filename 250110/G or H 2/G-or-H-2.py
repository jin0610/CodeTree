### 구간 단위로 완전탐색 / G or H 2
n = int(input())
arr = [input().split() for _ in range(n)]
arr = [[int(arr[i][0]),arr[i][1]] for i in range(n)]
arr.sort(key=lambda x:x[0])

# Write your code here!
result = 0
for i in range(n):
    cntG = 0
    cntH = 0
    for j in range(i, n):
        if arr[j][1] == "G":
            cntG += 1
        elif arr[j][1] == "H":
            cntH +=1

        if cntG == cntH:
            dist = arr[j][0] - arr[i][0]
            result = max(result, dist)

print(result)
