import sys

N = int(input())

if N == 1:
    print(1)
    sys.exit(0)

signs = []
for _ in range(N):
    n =int(input())
    if n < 0:
        signs.append(-1)
    else:
        signs.append(1)

# 부호
max_cnt = 0
cnt = 1
for n in range(1,N):
    
    if signs[n-1] == signs[n]:
        cnt += 1
    else:
        cnt = 1
    max_cnt = max(max_cnt, cnt)

print(max_cnt)