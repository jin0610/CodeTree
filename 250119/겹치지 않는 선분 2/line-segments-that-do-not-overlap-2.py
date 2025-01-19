### 물체 단위로 완전탐색 / 겹치지 않는 선분2
n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

# Write your code here!
cnt = 0

for i in range(n):
    i_x1, i_x2 = lines[i]
    check = 0
    for j in range(n):
        if i == j:
            continue
        j_x1, j_x2 = lines[j]
        if (j_x1 > i_x1 and j_x2 > i_x2)  or (j_x1 < i_x1 and j_x2 < i_x2):
            check += 1
    if check == (n - 1):
        cnt+=1
print(cnt)