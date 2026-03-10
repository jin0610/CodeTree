n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
_max_point = sorted(intervals, key = lambda x : -x[1])[0]

check = [0] * (_max_point[1] + 1)
for x1, x2 in intervals:
    check[x1] += 1
    check[x2] -= 1

answer = 0
for i in range(_max_point[1]):
    answer = max(answer, sum(check[:i + 1]))

print(answer)