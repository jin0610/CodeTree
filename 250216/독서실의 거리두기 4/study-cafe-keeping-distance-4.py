### 완전탐색 / 독서실의 거리두기 4
N = int(input())
seat = list(map(int, list(input())))

# Write your code here!
answer = 0
for i in range(N-1):
    if seat[i] == 1:
        continue
    for j in range(i+1, N):
        if seat[j] == 1:
            continue

        flag = False
        idx = 0
        dist = 101
        for k in range(N):    
            
            if (seat[k] == 1 or i == k or j == k):
                if flag == False:
                    flag = True
                    idx = k
                else:
                    dist = min(dist, abs(idx - k))
                    idx = k
        answer = max(answer, dist)

print(answer)