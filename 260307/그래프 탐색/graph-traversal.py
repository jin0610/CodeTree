n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
graph = [[0] * (n + 1) for _ in range(n+1)]
visited = [False] * (n+1)

for x, y in edges:
    graph[x][y] = 1
    graph[y][x] = 1

def dfs(v):
    global graph, visited, n, m


    for curr_v in range(1, n + 1):
        if graph[v][curr_v] == 1 and not visited[curr_v]:
            visited[curr_v] = True
            dfs(curr_v)

dfs(1)
print(sum(visited) - 1)

