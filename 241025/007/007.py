class _007:
    def __init__(self, code, point, time):
        self.code = code
        self.point = point
        self.time = time


code, point, time = input().split()
place1 = _007(code, point, time)

print("secret code :",place1.code)
print("meeting point :",place1.point)
print("time :", place1.time)