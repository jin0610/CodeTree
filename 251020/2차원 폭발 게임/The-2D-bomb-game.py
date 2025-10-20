import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

def explode_once(g):
    """한 번의 '폭발+중력'을 수행. 변화가 있으면 True 반환."""
    changed = False
    Nlen = N

    # 열 단위로 처리
    for c in range(Nlen):
        col = [g[r][c] for r in range(Nlen)]
        # run 탐색: 제거 마스크
        remove = [False]*Nlen

        r = 0
        while r < Nlen:
            if col[r] == 0:
                r += 1
                continue
            val = col[r]
            start = r
            r += 1
            while r < Nlen and col[r] == val:
                r += 1
            length = r - start
            if length >= M:
                changed = True
                for i in range(start, r):
                    remove[i] = True

        if changed:
            # 중력: 제거되지 않은 값만 아래로 내림
            kept = [col[i] for i in range(Nlen) if not remove[i] and col[i] != 0]
            zeros = [0]*(Nlen - len(kept))
            new_col = zeros + kept
            for r in range(Nlen):
                g[r][c] = new_col[r]

    return changed

def bomb(g):
    # 변화 없을 때까지 반복
    while explode_once(g):
        pass

def rotate_90_cw(g):
    # 90도 시계 회전: zip 기반 O(N^2)
    # 회전 후 바로 중력 한 번
    ng = [list(row) for row in zip(*g[::-1])]
    # 중력만 빠르게 한 번 더 (열 단위 압축)
    for c in range(N):
        col = [ng[r][c] for r in range(N)]
        kept = [x for x in col if x != 0]
        zeros = [0]*(N - len(kept))
        new_col = zeros + kept
        for r in range(N):
            ng[r][c] = new_col[r]
    return ng

for _ in range(K):
    bomb(grid)
    grid = rotate_90_cw(grid)
bomb(grid)

# 남은 블록 수
cnt = sum(1 for r in range(N) for c in range(N) if grid[r][c] != 0)
print(cnt)
