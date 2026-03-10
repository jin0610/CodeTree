import sys
n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
_min = -sys.maxsize
answer = _min
_sum = 0
for i in range(n):
    _sum += a[i]
    if _sum < 0:
        answer = max(answer, a[i])
        _sum = 0
    else:
        answer = max(answer, _sum)
       
print(answer)