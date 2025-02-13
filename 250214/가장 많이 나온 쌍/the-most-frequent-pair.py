n, m = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(m)]

# Write your code here!
answer = 0
for i in range(m):
    cnt = 0
    a, b = pairs[i]
    for j in range(m):
        if a in pairs[j] and b in pairs[j]:
            cnt += 1

    answer = max(answer, cnt)
print(answer)
