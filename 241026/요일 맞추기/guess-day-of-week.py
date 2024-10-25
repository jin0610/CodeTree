m1, d1, m2, d2 = map(int, input().split())

m_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

day1 = sum(m_days[:m1]) + d1
day2 = sum(m_days[:m2]) + d2

day = day2 - day1
print(days[day % 7])