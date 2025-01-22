### 물체단위로 완전탐색 / 선분 3개 지우기
N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]

# Write your code here!
result = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j + 1, N):
            count = [0] * 101
            overlap = True
            for l in range(N):
                if l == i or l == j or l == k:
                    continue
                x1, x2 = points[l]
                for x in range(x1, x2 + 1):
                    count[x] += 1
                    if count[x] > 1:
                        overlap = False
                        break
                    if not overlap:
                        break
            if overlap:
                result +=1
print(result)
# result = 0
# for i in range(N-2):
#     for j in range(i+1, N-1):
#         for k in range(j + 1, N):
#             count = [0] * 101
#             for l in range(N):
#                 if l == i or l == j or l == k:
#                     continue
#                 x1, x2 = points[l]
#                 for x in range(x1, x2 + 1):
#                     count[x] += 1
#             if set(count) == {0,1} or set(count) == {1} :
#                 result += 1
# print(result)
