### 완전탐색 / 좌표평면 위의 균형2
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Write your code here!
answer = 100
for i in range(1, 51):
    for j in range(1, 51):
        cnt_nw, cnt_ne, cnt_sw, cnt_se = 0,0,0,0
        for x, y in points:
            if x > i * 2  and y < j * 2:
                cnt_nw += 1

            if x > i * 2  and y > j * 2:
                cnt_ne += 1

            if x < i * 2  and y < j * 2:
                cnt_sw += 1
            
            if x < i * 2  and y > j * 2:
                cnt_se += 1

        cnt = max(cnt_nw, cnt_ne, cnt_sw, cnt_se)
        answer = min(answer, cnt)

print(answer)


            
