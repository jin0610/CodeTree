class Student:
    def __init__(self, name, height, weight):
        self.name= name
        self.height = height
        self.weight = weight

students = []
for i in range(5):
    name, height, weight = input().split()
    height = int(height)
    students.append(Student(name, height, weight)) 

students.sort(key=lambda x: (x.name))

print("name")
for i in range(5):
    print(f"{students[i].name} {students[i].height} {students[i].weight}")

students.sort(key=lambda x: (x.height),reverse=True)
print("\nheight")
for i in range(5):
    print(f"{students[i].name} {students[i].height} {students[i].weight}")