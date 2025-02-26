### Chapter 09. 케이스별로 나누기 - 좋은 전략 추려내기 / 독서실의 거리두기 2
import sys

N = int(input())
seats = list(map(int,list(input())))

def cal_dist(seat):
    min_dist = 1000
    max_dist = 0
    pre_idx = seat.index(1)
    for i in range(N):
        if seat[i] == 1 and pre_idx != i:
            dist = i - pre_idx
            min_dist = min(min_dist, dist)
            max_dist = max(max_dist, dist)
            pre_idx = i
    return min_dist, max_dist

answer = 0

# 기존의 좌석 배치에서 사람이 1명 앉아있을 경우
if seats.count(1) == 1:
    index = seats.index(1)
    print(max(index, N -1 -index))
    sys.exit()


# 기존의 좌석 배치에서 사람이 1명 앉아있을 경우
min_dist, max_dist = cal_dist(seats)

answer = min(min_dist, max_dist // 2)

# 첫 좌석에 사람이 앉아있지 않을 경우 앉아있다고 가정했을 때
if seats[0] == 0:
    seats2 = seats.copy()
    seats2[0] = 1
    min_dist2, _ = cal_dist(seats2)
    answer = max(answer, min_dist2)

# Case 3. 끝에 사람이 앉아있지 않을 경우 (처음은 1, 끝은 0일 경우)
if seats[-1] == 0:
    seats2 = seats.copy()
    seats2[-1] = 1
    min_dist2, _ = cal_dist(seats2)
    answer = max(answer, min_dist2)

print(answer)

    

