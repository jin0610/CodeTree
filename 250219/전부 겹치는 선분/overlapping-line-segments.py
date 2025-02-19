### 케이스 별로 나누기 / 전부 겹치는 선분

### 풀이 2.
N = int(input())

max_x1 = 0
min_x2 = 100
for i in range(N):
    x1, x2 = map(int, input().split())
    max_x1 = max(max_x1, x1)
    min_x2 = min(min_x2, x2)

if max_x1 <= min_x2:
    print("Yes")
else:
    print("No")

### 풀이 1, 선분이 겹칠 경우의 선 찾기
# N = int(input())
# points = [map(int,input().split()) for _ in range(N)]

# def intersecting(x1, x2, a1, a2):
#     if x1 > a2 or x2 < a1:
#         return False
#     else:
#         return True

# answer = "Yes"
# x1, x2 = points[0]
# for i in range(1, N):
#     a1, a2 = points[i]
#     if intersecting(x1, x2, a1, a2):
#         x1, x2 = max(x1, a1), min(x2, a2)
#     else:
#         answer = "No"
#         break


# print(answer)
