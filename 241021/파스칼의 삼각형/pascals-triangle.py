n = int(input())

arr = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(i+1):
        if(j == 0):
            arr[i][j] = 1
        else:
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
        print(arr[i][j], end = " ")
    print()