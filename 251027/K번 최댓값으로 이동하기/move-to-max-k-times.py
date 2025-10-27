from collections import deque
N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
r, c = map(int, input().split())

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def can_go(x, y, num):
    return in_range(x, y) and not visited[x][y] and grid[x][y] < num


# 1. 시작 위치(r -1, c-1)에 적혀있는 숫자 x 보다 작은 곳으로 이동
def bfs(curr_pos, num):

    global visited
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque([curr_pos])
    visited[curr_pos[0]][curr_pos[1]] = True

    min_max = 0   # 다음 기준이 될 주변의 작은 숫자 중 최댓값과 위치
    pos = [curr_pos]
    while q:
        cx, cy = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = cx + dx, cy + dy
            if can_go(nx, ny, num):
                q.append((nx, ny))
                visited[nx][ny] = True

                if grid[nx][ny] < num:
                    if grid[nx][ny] > min_max:
                        min_max = grid[nx][ny]
                        pos=[(nx, ny)]
                    elif grid[nx][ny]== min_max:
                        pos.append((nx, ny))

    pos = sorted(pos, key = lambda x:(x[0], x[1]))
    return min_max, pos[0]

base = grid[r-1][c-1]
base_pos = (r - 1, c - 1)

for _ in range(K):
    visited = [[False for _ in range(N)] for _ in range(N)]
    
    base, base_pos = bfs(base_pos, base)

print(base_pos[0] + 1, base_pos[1] + 1)
# 작은 숫자중 최댓값으로 이동(행, 열 작은 곳)
# 2. K 번 반복후 위치 r,c 출력