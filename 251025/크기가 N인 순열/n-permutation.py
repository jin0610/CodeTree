n = int(input())
visited = [False] * (n + 1)

seq = []
def sequence(curr_num):

    if curr_num == n + 1:
        print(*seq)
        return

    for i in range(1, n + 1):
        if visited[i]:
            continue

        visited[i] = True
        seq.append(i)

        sequence(curr_num + 1)

        seq.pop()
        visited[i] = False

    return

sequence(1)