import sys
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n

def get_minimum():
    global grid, idx

    _min = sys.maxsize
    for i in range(n):
        _min = min(_min, grid[i][idx[i]])
    return _min

idx = []
answer = 0
def min_maximun(curr_num):
    global idx, answer

    if curr_num == n:
        answer = max(answer, get_minimum())
        return

    for i in range(n):
        if visited[i]:
            continue

        visited[i] = True
        idx.append(i)

        min_maximun(curr_num + 1)

        idx.pop()
        visited[i] = False

    return

min_maximun(0)
print(answer)