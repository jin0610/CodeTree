### 케이스 별로 나누기 / 두 선분
x1, x2, x3, x4 = map(int, input().split())

# Write your code here!
# x2가 x3보다 작을 경우, x1이 x4보다 클 경우 겹치지 않은 것으로 판단
if x2 < x3 or x1 > x4:
    print("nonintersecting")
else:
    print("intersecting")