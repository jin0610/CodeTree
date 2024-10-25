import sys
a, b, c = map(int, input().split())

if (a < 11) or (a == 11 and b < 11) or (a == 11 and b == 11 and c < 11):
    print(-1) 
    sys.exit(0)

day1 = 11 + (11 * 60) + (11 * 24 * 60)
day2 = c + (b * 60) + (a * 24 * 60)

print(day2 - day1)