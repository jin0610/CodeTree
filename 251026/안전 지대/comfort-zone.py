n, m = map(int, input().split())
# 마을의 높이
town_heights = [list(map(int, input().split())) for _ in range(n)]

# 높이가 K 이하이면 False, 초과하면 True
town = [ [True for _ in range(m)] for _ in range(n)]

# N x M 범위 내인지 확인하는 함수
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# x, y로 갈 수 있는 지 판단하는 함수
def can_go(x, y, K):    # K : 수위
    if not in_range(x, y):
        return False

    if not visited[x][y] and town_heights[x][y] > K:
        return True

    return False

# 영역 새는 dfs 함수
def dfs(x, y, K):
    global visited
    
    visited[x][y] = True

    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny, K):
            dfs(nx, ny, K)

K, max_K = 1, 1   # 수위, 최대 높이
max_safe_area = 1   # 최대 안전영역 수
while K < 100:
    safe_area = 0   # 안전 영역 수

    # 방문 여부
    visited = [ [False for _ in range(m)] for _ in range(n)]

    for x in range(n):
        for y in range(m):
            if can_go(x, y, K):
                safe_area += 1
                dfs(x, y, K)

    if safe_area > max_safe_area:
        max_safe_area = safe_area
        max_K = K
    K += 1

print(max_K, max_safe_area)