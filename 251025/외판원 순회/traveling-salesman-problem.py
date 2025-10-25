import sys
N = int(input())
A = [
    list(map(int, input().split()))
    for _ in range(N)
]
visited = [False] * N
visited[0] = True
def calc_cost():
    global points

    cost = 0
    pre_point = 0
    for p in points:
        if A[pre_point][p] == 0:
            return  sys.maxsize
        cost += A[pre_point][p]
        pre_point = p
    cost += A[pre_point][0]
    return cost

points = []
answer = sys.maxsize
def choose_point(curr_num):
    global visited, points, answer

    if curr_num == N:
        answer = min(answer, calc_cost())
        return

    for n in range(1, N):
        if visited[n]:
            continue
        
        points.append(n)
        visited[n] = True
        
        choose_point(curr_num + 1)

        points.pop()
        visited[n] = False

    return

choose_point(1)
print(answer)