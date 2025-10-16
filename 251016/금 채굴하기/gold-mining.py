N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
dr, dc = [0, 1, 0, -1], [-1, 0, 1, 0] # 오른쪽 시계방향

def in_range(x, y):
    if x >= 0 and x < N and y >= 0 and y < N:
        return True
    return False

# 0 <= K <= N
result = 0 # 금의 개수
for i in range(N):
    for j in range(N):
        for k in range(N+1):
            cost = k ** 2 + (k + 1) ** 2
            gold = 0 # 금의 개수
            
            for x in range(N):
                for y in range(N):
                    if abs(i - x) + abs(j - y) == k:
                        gold += grid[x][y]
            if cost < M * gold:
                result = max(result, gold)

print(result)