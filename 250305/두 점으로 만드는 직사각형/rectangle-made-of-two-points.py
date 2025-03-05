### Ad-hoc (고려해야할 대상이 뚜렷해지는 경우) / 두 점으로 만드는 직사각형
x1, y1, x2, y2 = map(int,input().split())
a1, b1, a2, b2 = map(int,input().split())

# 밑변
base = max(a2, x2) - min(x1, a1)

# 높이
height = max(y2,b2) - min(y1, b1)

print(base * height)