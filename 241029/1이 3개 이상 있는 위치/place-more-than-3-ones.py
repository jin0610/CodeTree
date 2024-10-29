n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def in_range(x, y):
    return x >= 0 and x < n  and y >= 0 and y < n

result = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for z in range(4):
            x, y = i + dx[z], j + dy[z]
            if in_range(x, y) and arr[x][y] == 1:
                cnt += 1
        if cnt >= 3:
            result +=1 

print(result)