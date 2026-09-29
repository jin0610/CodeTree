n, t = map(int, input().split())
left = list(map(int, input().split()))
right = list(map(int, input().split()))
down = list(map(int, input().split()))

for _ in range(t):
    temp1 = left[-1]
    for i in range(n-1, 0, -1):
        left[i] = left[i - 1]
    left[0] = down[-1]

    temp2 = right[-1]
    for i in range(n-1, 0, -1):
        right[i] = right[i - 1]
    right[0] = temp1

    for i in range(n-1, 0, -1):
        down[i] = down[i - 1]
    down[0] = temp2

print(*left)
print(*right)
print(*down)