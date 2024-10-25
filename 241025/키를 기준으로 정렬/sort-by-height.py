class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())

info = []
for _ in range(n):
    name, height, weight = input().split()
    info.append(Person(name, height, weight)) 

info.sort(key=lambda x: x.height)

for i in range(n):
    print(f"{info[i].name} {info[i].height} {info[i].weight}")