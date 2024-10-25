a, b, c, d = map(int, input().split())
time = (c-a) * 60 + (d-b)
print(time)
# hours, mins = a, b
# time = 0
# while True:

#     if a == c and b == d:
#         print(time)
#         break

#     else:
#         time += 1
#         mins += 1

#         if mins == 60:
#             hours += 1
#             mins = 0