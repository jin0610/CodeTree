n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
cnt = 0
while cnt != t:
    temp = u[-1]
    for i in range(n - 1, 0, -1):
        u[i] = u[i - 1]

    u[0] = d[-1]
    for i in range(n - 1, 0, -1):
        d[i] = d[i - 1]
    
    d[0] = temp
    cnt += 1

print(*u)
print(*d)