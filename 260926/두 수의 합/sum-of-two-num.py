from collections import defaultdict
N, K = map(int, input().split())
arr = list(map(int, input().split()))

num_dict = defaultdict(int)
cnt = 0

for n in arr:
    diff = K - n

    if diff in num_dict:
        cnt += num_dict[diff]

    num_dict[n] += 1

print(cnt)