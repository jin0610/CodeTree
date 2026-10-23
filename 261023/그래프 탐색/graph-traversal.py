n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
graph = [[0] * n for _ in range(n)]
for x, y in edges:
    x -= 1
    y -= 1
    graph[x][y] = 1
    graph[y][x] = 1

visited =[0] * n 
cnt = 0
def dfs(v):
    global graph, visited, cnt
    for next_v in range(n):
        if graph[v][next_v] and not visited[next_v]:
            visited[next_v] = 1
            cnt += 1
            dfs(next_v)


visited[0] = 1
dfs(0)

print(sum(visited) - 1)