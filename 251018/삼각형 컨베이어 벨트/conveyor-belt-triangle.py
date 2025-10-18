n, t = map(int, input().split())

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
for _ in range(t):
    temp = l[-1]
    for i in range(n-1, 0, -1):
        l[i] = l[i - 1]
    l[0] = d[-1]

    temp2 = r[-1]
    for i in range(n-1, 0, -1):
        r[i] = r[i - 1]
    r[0] = temp

    l[0] = d[-1]
    for i in range(n-1, 0, -1):
        d[i] = d[i - 1]
    d[0] = temp2
print(*l)
print(*r)
print(*d)