### 케이스 별로 나누기 / 전부 겹치는 선분
N = int(input())
points = [map(int,input().split()) for _ in range(N)]

def intersecting(x1, x2, a1, a2):
    if x1 > a2 or x2 < a1:
        return False
    else:
        return True

answer = "Yes"
x1, x2 = points[0]
for i in range(1, N):
    a1, a2 = points[i]
    if intersecting(x1, x2, a1, a2):
        x1, x2 = max(x1, a1), min(x2, a2)
    else:
        answer = "No"
        break


print(answer)
