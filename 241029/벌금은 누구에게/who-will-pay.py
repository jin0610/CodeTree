N, M, K = map(int, input().split())
s =[0] * (N + 1)

result = -1
for i in range(M):
    cnt = int(input())

    s[cnt] += 1

    if K in s:
        result = s.index(K)
        break

print(result)