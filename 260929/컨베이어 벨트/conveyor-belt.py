n, t = map(int, input().split())
up = list(map(int,input().split()))
down = list(map(int, input().split()))

# t초동안 회전
for _ in range(t):
    temp = up[-1]
    for i in range(n-1, 0, -1):
        up[i] = up[i-1]
    
    up[0] = down[-1]
    for i in range(n - 1, 0, -1):
        down[i] = down[i - 1]
    down[0] = temp

print(*up)
print(*down)