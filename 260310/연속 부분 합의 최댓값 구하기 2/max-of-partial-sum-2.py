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
        _sum = a[i]
    answer = max(answer, _sum)
    # if _sum > answer:
    #     _sum += a[i]
    #     answer = max(answer, _sum)
    # else:
    #     if a[i] < 00:
            
       
print(answer)