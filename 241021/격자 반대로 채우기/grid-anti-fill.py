n = int(input())

result = [[0] * n for _ in range(n)]

num = 1
for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        if(i % 2 == 1):
            
            result[j][i] = num
        else:
            result[n-j-1][i] = num
        num += 1

for i in range(n):
    print(*result[i])