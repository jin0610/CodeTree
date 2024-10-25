class Student:
    def __init__(self, name, height, weight):
        self.name= name
        self.height = height
        self.weight = weight

n = int(input())
students = []
for i in range(n):
    name, height, weight = input().split()
    height, weight = int(height), int(weight)
    students.append(Student(name, height, weight)) 

students.sort(key=lambda x: (x.height, -x.weight))

for i in range(n):
    print(f"{students[i].name} {students[i].height} {students[i].weight}")