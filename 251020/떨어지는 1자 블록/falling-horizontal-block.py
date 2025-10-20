n, m, k = map(int, input().split())
grid = [
    list(map(int, input().split())) 
    for _ in range(n)
]

k = k - 1

def in_range(r, c):
    return r >= 0 and r < n and c >= 0 and c < n

block_r = 0
while True:
    stopped = False
    for c in range(k, k + m):
        if not in_range(block_r + 1, c) or grid[block_r + 1][c] == 1:
            stopped = True
            break
        
    if stopped == True:
        break
    
    block_r += 1

for c in range(k, k + m):
    grid[block_r][c] = 1

for r in range(n):
    print(*grid[r])


