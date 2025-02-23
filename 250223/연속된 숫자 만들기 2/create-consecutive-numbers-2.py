### 케이스 별로 나누기(상황에 따른 최선의 움직임) / 연속된 숫자 만들기 2
A, B, C = map(int, input().split())

cnt = 0
while True:
    if abs(B - A) == 1 and abs(C - B) == 1:
        break
    
    if abs(B - A) == 2 or abs(C - B) == 2:
        cnt += 1
        break

    if abs(B - A) >= abs(C - B):
        A, B = B, (B + C) // 2
    else:
        C, B = B, (A + B) // 2

    cnt += 1

print(cnt)
