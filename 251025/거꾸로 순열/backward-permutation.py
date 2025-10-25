n = int(input())
visited = [False] * (n + 1)

answer = []
def sequence(curr_num):
    global answer

    if curr_num == n + 1:
        print(*answer)
        return

    for i in range(n, 0, -1):
        if visited[i]:
            continue

        visited[i] = True
        answer.append(i)
        
        sequence(curr_num + 1)

        answer.pop()
        visited[i] = False

sequence(1)