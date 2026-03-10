n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# _max_point = sorted(intervals, key = lambda x : -x[1])[0]

check = [0] * (20001)
_max = 0
for x1, x2 in intervals:
    _max = max(_max, x2)
    check[x1] += 1
    check[x2] -= 1

answer = 0
for i in range(_max):
    answer = max(answer, sum(check[:i + 1]))

print(answer)