n, m = map(int, input().split())
grid = [list(map(int,input().split())) for _ in range(n)]

answer = -1
def is_in_minus(r1, c1, r2, c2):
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            if grid[r][c] <= 0:
                return True

    return False

for r1 in range(n):
    for c1 in range(m):
        for r2 in range(r1, n):
            for c2 in range(c1, m):
                if not is_in_minus(r1, c1, r2, c2):
                    rectangle_size = (r2 - r1 + 1 ) * (c2 - c1 + 1)
                    answer = max(answer, rectangle_size)

print(answer)