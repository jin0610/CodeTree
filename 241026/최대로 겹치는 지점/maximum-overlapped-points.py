N = int(input())

result = [0] * 100
for n in range(N):
    x1, x2 = map(int, input().split())

    for x in range(x1-1, x2):
        result[x] += 1

print(max(result))