import sys
n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
answer = -sys.maxsize
_sum = 0
for i in range(n):
    if _sum < 0:
        _sum = a[i]
    else:
        _sum += a[i]
    answer = max(answer, _sum)
    # _sum += a[i]
    # if _sum < 0:
    #     answer = max(answer, a[i])
    #     _sum = 0
    # else:
    #     answer = max(answer, _sum)
       
print(answer)