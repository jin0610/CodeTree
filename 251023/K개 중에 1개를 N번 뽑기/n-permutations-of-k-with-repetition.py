N, K = map(int, input().split())

nums =[]
def choose(num):
    if num == K + 1:
        print(*nums)
        return

    for i in range(1, N + 1):
        nums.append(i)
        choose(num + 1)
        nums.pop()

    return

choose(1)