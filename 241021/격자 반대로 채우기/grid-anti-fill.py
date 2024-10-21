n = int(input())

result = [[0] * n for _ in range(n)]

num = 1

for col in range(n-1, -1, -1):
    for row in range(n-1, -1, -1):
        if(n - 1 - col) % 2 == 0:
            result[row][col] = num
        else:
            result[n-row-1][col] = num
        num = num + 1
        

for i in range(n):
    print(*result[i])