n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
answer = 0

def find_max_xor(curr_idx, cnt, curr_val):
    global answer

    if cnt == m:
        answer = max(answer, curr_val)
        return

    if curr_idx >= n or n - curr_idx < m - cnt:
        return

    find_max_xor(curr_idx + 1, cnt + 1, curr_val ^ A[curr_idx])
    find_max_xor(curr_idx + 1, cnt, curr_val)

find_max_xor(0, 0, 0)
print(answer)