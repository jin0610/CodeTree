### 케이스 별로 나누기 (가능한 상황을 나열하기) - L, R 그리고 B
board = [list(input()) for _ in range(10)]

# Please write your code here.
B, R, L = [],[],[]
for i in range(10):
    if 'B' in board[i]:
        B.append(i)
        B.append(board[i].index('B'))

    if 'R' in board[i]:
        R.append(i)
        R.append(board[i].index('R'))
        
    if 'L' in board[i]:
        L.append(i)
        L.append(board[i].index('L'))

print(abs(B[0] - L[0]) + abs(B[1] - L[1])-1)