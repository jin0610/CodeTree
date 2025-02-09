### 잘 모르는 상황에서의 완전탐색 / 야바위
n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]

# Write your code here!
max_cnt = 0
for i in range(3):
    cnt = 0
    position = [0, 0, 0]
    position[i] = 1
    for a, b, c in moves:
        position[a - 1], position[b - 1] = position[b - 1], position[a - 1]
        if position[c - 1] == 1:
            cnt += 1
        
    max_cnt = max(max_cnt, cnt)
print(max_cnt)