### 구간 단위로 완전 탐색 / G or H 3
import sys
n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Write your code here!
arr = [0] * (max(x)+1)
for i in range(len(x)):
    if c[i] == "G":
        arr[x[i]] = 1
    else:
        arr[x[i]] = 2

result = -sys.maxsize
for i in range(1, len(arr) - k + 2):

    result = max(result, sum(arr[i:i+k +1]))
print(result)

