### 완전탐색 / 독서실의 거리두기 4
N = int(input())
seat = list(map(int, list(input())))

# Write your code here!
answer = 0
for i in range(N-1):
    for j in range(i + 1, N):
        temp = seat.copy()
        if seat[i] == 1 or seat[j] == 1:
            continue
        temp[i] = 1
        temp[j] = 1
        idx = []
        dist = 1000
        for k in range(N):
            if seat[k] == 1:
                idx.append(k)

        for k in range(len(idx)-1):
            dist = min(dist, abs(idx[k+1] - idx[k]))

        answer = max(answer, dist)

print(answer-1)