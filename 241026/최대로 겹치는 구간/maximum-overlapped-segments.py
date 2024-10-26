N = int(input())

result = [0] * 201
for n in range(N):
    x1, x2 = map(int, input().split())
    x1, x2 = x1 + 100, x2 + 100
    for x in range(x1, x2+1):
        result[x] += 1

print(max(result))