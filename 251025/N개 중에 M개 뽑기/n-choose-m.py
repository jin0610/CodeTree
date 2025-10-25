N, M = map(int, input().split())

numbers = []
def find_comb(start, cnt):
    if cnt == M:
        print(*numbers)
        return

    for i in range(start, N + 1):
        if i in numbers:
            continue
        numbers.append(i)
        find_comb(i + 1, cnt + 1) 
        numbers.pop()

    return

find_comb(1, 0)