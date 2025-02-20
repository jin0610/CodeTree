### 케이스별로 나누기 / 전부 겹치는 선분2
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Write your code here!
for i in range(n):
    min_x2 = 100
    max_x1 = 0
    for j in range(n):
        if i == j:
            continue
        x1, x2 = segments[j]
        min_x2 = min(min_x2, x2)
        max_x1 = max(max_x1, x1)

    if min_x2 >= max_x1:
        answer="Yes"
        break
    else:
        answer="No"

print(answer)