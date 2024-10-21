n = int(input())

result = [[0] * n for _ in range(n)]

num = n*n
for i in range(n):
    for j in range(n):
        if (n %2 == 1):
            if(i % 2 == 0):
                result[j][i] = num
            else:
                result[n-j-1][i] = num
        else:
            if(i % 2 == 0):
                result[n-j-1][i] = num
            else:
                result[j][i] = num

        num = num - 1

for i in range(n):
    print(*result[i])