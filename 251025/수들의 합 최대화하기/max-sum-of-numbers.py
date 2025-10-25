import sys

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n

def get_sum():
    global colored
    
    result = 0
    for i in range(n):
        result += grid[i][colored[i]]
    
    return result

colored = []
answer = -sys.maxsize
def get_max_sum(curr_num):
    global colored, answer

    if curr_num == n:
        answer = max(answer, get_sum())
        return

    for i in range(n):
        if visited[i]:
            continue

        visited[i] = True
        colored.append(i)
        get_max_sum(curr_num + 1)

        colored.pop()
        visited[i] = False

    return

get_max_sum(0)
print(answer)