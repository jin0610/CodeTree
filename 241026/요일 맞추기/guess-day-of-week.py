m1, d1, m2, d2 = map(int, input().split())

m_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

day = 0
for i in range(m1, m2):
    day += m_days[i]

day = day - d1 + d2

print(days[day % 7])