n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def check():
    d = [[1e9]*n for _ in range(n)]
    d[0][0] = graph[0][0]

    for j in range(1, n):
        d[0][j] = max(d[0][j-1], graph[0][j])
    
    for i in range(1, n):
        d[i][0] = max(d[i-1][0], graph[i][0])

    for i in range(1, n):
        for j in range(1, n):
            d[i][j] = max(min(d[i-1][j], d[i][j-1]), graph[i][j])
    
    return d[n-1][n-1]  # 1e9면 경로 없음!


res = 1e9  # |최대-최소| 최소!
for low in range(1, 101):
    for i in range(n):
        for j in range(n):
            if graph[i][j] < low:
                graph[i][j] = 1e9

    ans = check()
    if ans < 1e9:
        res = min(res, abs(ans-low))

print(res)