from sortedcontainers import SortedSet
n, m = map(int, input().split())
queries = list(map(int, input().split()))

nums = SortedSet([i + 1 for i in range(m)])
for elem in queries:
    nums.remove(elem)
    print(nums[-1])


