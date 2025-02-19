### 케이스 별로 나누기 / 구역 청소
a, b = map(int, input().split())
c, d = map(int, input().split())

# Write your code here!
answer = 0
# 두 case가 겹치지 않은 경우 [a,b] + [c,d]
if d < a or b < c:
    print((b - a) + (d - c))
else:
    print(max(b, d) - min(a, c))