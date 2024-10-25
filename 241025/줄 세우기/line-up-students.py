class Student:
    def __init__(self, idx, height, weight):
        self.idx= idx
        self.height = height
        self.weight = weight

n = int(input())

students = []
for i in range(n):
    height, weight = map(int,input().split())
    students.append(Student(i + 1, height, weight)) 
    

students.sort(key=lambda x: (x.height, x.weight, -x.idx), reverse=True)

for i in range(n):
    print(f"{students[i].height} {students[i].weight} {students[i].idx}")