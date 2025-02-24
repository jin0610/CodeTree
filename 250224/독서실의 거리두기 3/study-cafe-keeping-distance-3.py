### 케이스 별로 나누기 (좋은 전략 찾아내기 - 최선의 선택) / 독서실의 거리두기 3
N = int(input())
seats = list(input())

# Write your code here!
# step1. '1'이 놓인 index 번호 찾기
seats_idx = []
for i in range(N):
    if seats[i] == "1":
        seats_idx.append(i)

# step2.인접한 쌍들 중 가장 먼 1간의 길이 찾기
max_dist = 0
for i in range(len(seats_idx)-1):
    max_dist = max(max_dist, seats_idx[i + 1] - seats_idx[i])

# step3. 가장 먼 쌍의 위치 가운데에 '1' 놓기
answer = max_dist // 2

# step4. 인접한 쌍들 중 가장 가까운 1간의 길이 찾기
for i in range(len(seats_idx) - 1):
    answer = min(answer, seats_idx[i+1] - seats_idx[i])

print(answer)

