class Spy:
    def __init__(self, code, score):
        self.code = code
        self.score = score

idx = 0
spyInfo = []
for i in range(5):
    code, score = input().split()
    score = int(score)
    spyInfo.append(Spy(code, score))
    if spyInfo[i].score < spyInfo[idx].score:
        idx = i
    
        
    
print(spyInfo[idx].code, spyInfo[idx].score)