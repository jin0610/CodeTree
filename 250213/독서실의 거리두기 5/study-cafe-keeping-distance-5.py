### 완전탐색 / 독서실의 거리두기 5
N = int(input())
seat = list(map(int,list(input())))

# Write your code here!

idx = []
for i in range(N):
    if seat[i] == 1:
        idx.append(i)

dist = []
if 0 not in idx:
    dist.append(abs(idx[0]))

if (N - 1) not in idx:
    dist.append(abs(idx[-1] - (N - 1)))

for i in range(len(idx)-1):
    diff = (idx[i] + idx[i + 1]) // 2
    dist.append(abs(diff - idx[i]))
    dist.append(abs(diff - idx[i + 1]))

print(max(dist))
