m1, d1, m2, d2 = map(int, input().split())
A = input()

m_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

day = (sum(m_days[:m2]) + d2) - (sum(m_days[:m1]) + d1)
result = day // 7

if (day % 7) >= days.index(A):
    result = result + 1

print(result)