from collections import deque

N = int(input())

# 0. 정수를 deque에 넣기
dq = deque()
for n in range(N):
    dq.append(n + 1)

while len(dq) > 1:
    # 1. 맨 앞의 정수 제거
    dq.popleft()

    # 2. 남은 수열의 맨 앞의 정수를 맨 뒤로 이동
    dq.append(dq.popleft())

print(dq[0])


