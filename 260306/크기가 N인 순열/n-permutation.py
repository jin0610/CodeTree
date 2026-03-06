n = int(input())

# Please write your code here.
visited = [False] * (n + 1)
comb = []
def combs(cnt):
    global visited, comb

    if cnt == n:
        print(*comb)
        return

    for i in range(1, n + 1):
        if visited[i]:
            continue

        visited[i] = True
        comb.append(i)
        combs(cnt + 1)
        comb.pop()
        visited[i] = False

combs(0)



