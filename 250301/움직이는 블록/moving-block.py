### Ad-hoc (지극히 최선인 전략히 확실한 경) / 움직이는 블록
n = int(input())
blocks = [int(input()) for _ in range(n)]

# 평균 높이 구하기
mean_height = sum(blocks) // n
cnt = 0 # 움직이는 블럭 수
for i in range(n):
    if blocks[i] > mean_height:
        cnt += (blocks[i] - mean_height)

print(cnt)