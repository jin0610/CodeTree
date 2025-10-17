N = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(N)
]

# 1,2,3,4번 방향
dirs = [(-1, 1), (-1, -1), (1, -1), (1, 1)]
max_sum = 0 # 최대합

def in_range(x, y):
    return x >= 0 and x < N and y >= 0 and y < N

for i in range(N):
    for j in range(N):
        visited = [0, 0, 0, 0] # 각 방향 순회 여부
        num = 0  # 합
        cx, cy = j, i
        for d in range(4):
            move_cnt = 0
            while True:
                nx, ny = cx + dirs[d][1], cy + dirs[d][0]
                if in_range(nx, ny):
                    move_cnt += 1
                    num += grid[cy][cx]
                    cx, cy = nx, ny
                else:
                    break

            if move_cnt > 0:
                visited[d] = 1
            else:
                break
        
        if 0 not in visited:
            max_sum = max(max_sum, num)

print(max_sum)