### 완전탐색 / 독서실의 거리두기 5
N = int(input())
seat = list(map(int,list(input())))

# Write your code here!
answer = 0
for i in range(N):
    if seat[i] == 1:
        continue
    temp = seat.copy()
    temp[i] = 1
    idx = []
    dist = 20
    for j in range(N):
        if j == i:
            continue
        
        if temp[j] == 1:
            idx.append(abs(i-j))
    dist = min(idx)
    answer = max(answer, dist)

print(answer)

    