### 케이스 별로 나누기 (좋은 전략 찾아내기 - 최선의 선택) / 독서실의 거리두기 3
N = int(input())
seats = list(input())

# Write your code here!
seats_idx = []
for i in range(N):
    if seats[i] == "1":
        seats_idx.append(i)

max_dist = 0
cnt = 1
for i in range(len(seats_idx)-1):
    if max_dist == seats_idx[i+1] - seats_idx[i]:
        cnt += 1
    else:
        cnt = 1
    max_dist = max(max_dist, seats_idx[i + 1] - seats_idx[i])

answer = max_dist // 2
for i in range(len(seats_idx) - 1):
    answer = min(answer, seats_idx[i+1] - seats_idx[i])

print(answer)

