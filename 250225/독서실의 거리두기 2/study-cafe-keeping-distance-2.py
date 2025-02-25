### Chapter 09. 케이스별로 나누기 - 좋은 전략 추려내기 / 독서실의 거리두기 2
N = int(input())
seats = list(input())

# Step 1. seats의 '1'인 인덱스 추출
seats_idx = []
for i in range(N):
    if seats[i] == '1':
        seats_idx.append(i)

    # 마지막 번호가 1이 아닐 경우 N + 1을 추가
    if i == N - 1 and seats[i] != '1':
        seats_idx.append(N)

# Step 2. 각 간격 중 가장 긴 간격을 확인
max_dist = 0
for i in range(len(seats_idx)-1):
    dist = seats_idx[i + 1] - seats_idx[i]
    max_dist = max(max_dist, dist)

# Step 3. 가장 짧은 간격 출력
min_dist = max_dist // 2
for i in range(len(seats_idx)-1):
    dist = seats_idx[i + 1] - seats_idx[i]
    min_dist = min(min_dist, dist)

if N in seats_idx:
    seats_idx[-1] = N - 1
    dist = 1000
    for i in range(len(seats_idx)-1):
        dist = min(dist,seats_idx[i + 1] - seats_idx[i])
    min_dist = max(min_dist, dist)

print(min_dist)
    

