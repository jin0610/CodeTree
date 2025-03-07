### 완전탐색 / 훌륭한 점프
N, K = map(int, input().split())
stone = list(map(int,input().split()))

def is_possible(val):
    temp = []
    for i, elem in enumerate(stone):
        if elem <= val:
            temp.append(i)

    for i in range(1, len(temp)):
        dist = temp[i] - temp[i-1]
        if dist > K:
            return False
    
    return True

answer = 101
for i in range(100, max(stone[0], stone[-1])-1, -1):
    if is_possible(i):
        answer = min(answer, i)
        
print(answer)