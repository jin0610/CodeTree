class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

n = int(input())

scores = []
for _ in range(n):
    name, kor, eng, math = input().split()
    kor, eng, math = list(map(int, [kor, eng, math]))
    scores.append(Student(name, kor, eng, math)) 

scores.sort(key=lambda x: (x.kor + x.eng + x.math))

for i in range(n):
    print(f"{scores[i].name} {scores[i].kor} {scores[i].eng} {scores[i].math}")