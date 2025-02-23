### 케이스 별로 나누기(상황에 따른 최선의 움직임) / 연속된 숫자 만들기 2
A, B, C = map(int, input().split())

if abs(B - A) == 1 and abs(C - B) == 1:
    print(0)
    
elif abs(B - A) == 2 or abs(C - B) == 2:
    print(1)
else:
    print(2)