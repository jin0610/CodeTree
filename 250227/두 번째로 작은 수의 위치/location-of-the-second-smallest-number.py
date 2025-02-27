### 케이스 별로 나누기(가능한 상황을 나열하기) - 두번째로 작은 수의 위치
import sys

n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
# 두 번째로 작은 수가 없는 경우
if (len(set(a)) == 1):
    print(-1)
    sys.exit()

# 가장 작은 수 제거
a_del_min= [a[i] for i in range(n) if a[i] != min(a)]

# 두 번째로 작은 수가 여러개 있는 경우
min_2nd = min(a_del_min)
if a.count(min_2nd) != 1:
    print(-1)
    sys.exit()

# 두번째로 큰 수 출력
print(a.index(min_2nd) + 1)