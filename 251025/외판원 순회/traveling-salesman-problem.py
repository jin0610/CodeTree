import sys
n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n

def get_min_cost():
    global point

    cost = 0
    for i in range(n - 1):
        cost += A[point[i]][point[i + 1]]
    cost += A[point[-1]][0]

    return cost

point = [0]
answer = sys.maxsize
def traveling_saleman(curr_num):
    global visited, point, A, answer

    if curr_num == n:
        answer = min(answer, get_min_cost())
        return

    for i in range(1, n):
        if visited[i]:
            continue

        visited[i] = True
        point.append(i)
        traveling_saleman(curr_num + 1)

        point.pop()
        visited[i] = False

    return

traveling_saleman(1)
print(answer)