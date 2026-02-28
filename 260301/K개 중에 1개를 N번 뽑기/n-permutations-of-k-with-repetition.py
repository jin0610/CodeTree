K, N = map(int, input().split())

# Please write your code here.
num_list = []
def choose(curr_n):
    global N, K

    if curr_n == N:
        print(*num_list)
        return

    for i in range(1, K + 1):
        num_list.append(i)
        choose(curr_n + 1)
        num_list.pop()


choose(0)

