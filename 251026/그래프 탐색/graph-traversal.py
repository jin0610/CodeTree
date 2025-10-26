N, M = map(int, input().split())
edgs = [
    [0 for _ in range(N)]
    for _ in range(N)
]
for _ in range(M):
    x, y = map(int,input().split())
    edgs[x - 1][y - 1], edgs[y - 1][x - 1] = 1, 1

visited =  [False for _ in range(N)]
visited[0] = True

answer = 0
def dfs(curr_v):
    global answer, visited

    for next_v in range(N):
        if edgs[curr_v][next_v] and not visited[next_v]:
            answer += 1
            visited[next_v] = True
            dfs(next_v)

dfs(0)
print(answer)