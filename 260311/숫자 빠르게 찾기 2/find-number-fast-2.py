from sortedcontainers import SortedSet
n, m = map(int, input().split())
arr = list(map(int, input().split()))

s = SortedSet(arr)

for _ in range(m):
    n = int(input())
    try:
        idx = s.bisect_left(n)
        print(s[idx])
    except:
        print(-1)