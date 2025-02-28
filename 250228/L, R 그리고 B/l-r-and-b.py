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


dist = abs(B[0] - L[0]) + abs(B[1] - L[1]) -1

# B, L, R이 일직선 상에 있는 경우 2칸 돌아서 가므로 +2
if (B[1] < R[1] and R[1] < L[1]) or (B[1] > R[1] and R[1] > L[1]):
    if B[0] == R[0] and R[0] == L[0]:
        dist += 2
if (B[0] < R[0] and R[0] < L[0]) or (B[0] > R[0] and R[0] > L[0]):
    if B[1] == R[1] and  R[1] == L[1]:
        dist += 2

print(dist)