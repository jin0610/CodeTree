m1, d1, m2, d2 = map(int, input().split())

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day = 0

for i in range(m1, m2):
    day += days[i]

# m1월 1일부터 m1월 (d1-1)일 까지 제거 + d2일 더하기
day = day - (d1-1) + d2

print(day)