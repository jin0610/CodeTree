n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Write your code here!
for i in range(n):
    min_x = 100
    max_x = 0
    for j in range(n):
        if i == j:
            continue
        x1, x2 = segments[j]
        min_x = min(min_x, x2)
        max_x = max(max_x, x1)

    if min_x <= max_x:
        answer="Yes"
    else:
        answer="No"

print(answer)