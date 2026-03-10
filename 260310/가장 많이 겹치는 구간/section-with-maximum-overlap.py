n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# _max_point = sorted(intervals, key = lambda x : -x[1])[0]

points = []
_max = 0
for x1, x2 in intervals:
    points.append((x1, +1)) # 시작점
    points.append((x2, -1)) # 끝점

points.sort()

answer = 0
sum_val = 0
for x, v in points:
    sum_val += v
    
    if sum_val >= n:
        break
    
    answer = max(answer, sum_val)

print(answer)
