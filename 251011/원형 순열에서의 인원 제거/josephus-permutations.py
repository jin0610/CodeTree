from collections import deque

n, K = map(int,input().split())

dq = deque()

# 삽입
for i in range(n):
    dq.append(i + 1)

while len(dq) != 0:
    for k in range(K):
        if k + 1 == K:
            num = dq.popleft()
            print(num, end=" ")
        else:
            num = dq.popleft()
            dq.append(num)
