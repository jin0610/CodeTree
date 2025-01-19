### 물체 단위로 완전탐색 / 운행 되고 있는 시간
n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]

# Write your code here!

max_times = 0
for i in range(n):
    time_list = [0] * 1001
    time = 0
    for j in range(n):
        if i == j:
            continue
        for t in range(times[j][0],times[j][1]):
            if time_list[t] == 0:
                time_list[t] = 1
                time += 1
    max_times = max(max_times, time)
              

print(max_times)