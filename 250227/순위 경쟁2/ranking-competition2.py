### 케이스 별로 나누기(가능한 상황을 나열하기) - 순위 경쟁2
N = int(input())

honor = ""
changeCnt = 0
A_score = 0
B_score = 0
for i in range(N):
    c, s = input().split()
    s = int(s)

    if c == 'A':
        A_score += s
    else:
        B_score += s

    if i == 0:
        honor = 'AB'
        continue

    max_score = max(A_score, B_score)
    if max_score == A_score and max_score == B_score:
        if honor != 'AB':
            changeCnt += 1
        honor = 'AB'
    elif max_score == A_score:
        if honor != 'A':
            changeCnt += 1
        honor = "A"
    elif max_score == B_score:
        if honor != 'B':
            changeCnt += 1
        honor = "B"
    else:
        continue
        
        

print(changeCnt)