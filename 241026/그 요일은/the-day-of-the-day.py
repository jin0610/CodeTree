m1, d1, m2, d2 = map(int, input().split())
A = input()

m_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

day = (sum(m_days[:m2]) + d2) - (sum(m_days[:m1]) + d1)
# print(day, day //7, day %7, days.index(A))
if (day % 7) >= days.index(A):
    if(day // 7) == 0:
        print(day // 7)
    else:
        print(day // 7 + 1)
    
else:
    print(day // 7)