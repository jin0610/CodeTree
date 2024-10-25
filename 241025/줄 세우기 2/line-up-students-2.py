class Student:
    def __init__(self, idx, height, weight):
        self.idx = idx
        self.height = height
        self.weight = weight


N = int(input())

students = []
for n in range(N):
    height, weight = map(int, input().split())
    students.append(Student(n+1, height, weight))

students.sort(lambda x : (x.height, -x.weight))

for n in range(N):
    print(f"{students[n].height} {students[n].weight} {students[n].idx}")