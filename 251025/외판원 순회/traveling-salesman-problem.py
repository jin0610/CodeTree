import sys
N = int(input())
A = [
    list(map(int, input().split()))
    for _ in range(N)
]
visited = [False] * N
visited[0] = True
def calc_cost(channel):

    cost = 0
    pre_point = 0
    for point in channel:
        cost += A[pre_point][point]
        pre_point = point

    return cost

points = [0]
answer = sys.maxsize
def choose_point(curr_num, last):
    global visited, points, answer

    if curr_num == N:
        if A[last][0] != 0:
            answer = min(answer, calc_cost(points + [0]))
        return

    for n in range(1, N):
        if visited[n] or A[last][n] == 0:
            continue
        
        points.append(n)
        visited[n] = True
        
        choose_point(curr_num + 1, n)

        points.pop()
        visited[n] = False

    return

choose_point(1, 0)
print(answer)