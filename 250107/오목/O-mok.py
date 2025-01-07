### 자리 수 단위로 완전탐색 / 오목
import sys
board = [list(map(int, input().split())) for _ in range(19)]

# Write your code here!

def in_range(x, y):
    return x > 0 and y > 0 and x < 19 and y < 19 

def is_winner(cnt, winner, x, y):
    if cnt == 5:
        print(winner)
        print(x+1, y+1)
        sys.exit(0)

winner = 0
for row in range(19):
    for col in range(19):
        color = board[row][col]
        cnt = 0
        if color == 0:
            continue

        # 가로줄, 세로줄, 대각선 우, 대각선 좌
        for r in range(5):
            if in_range(row + r, col) and board[row + r][col] == color:
                cnt += 1
                x, y = (row + (row + r)) // 2, col
                is_winner(cnt, color, x, y)
            else:
                cnt = 0
                break
       

        for c in range(5):
            if in_range(row, col + c) and board[row][col + c] == color:
                cnt += 1
                x, y = row, (col + (col + c)) // 2
                is_winner(cnt, color, x, y)

            else:
                cnt = 0
                break

        for i in range(5):
            if in_range(row + i, col + i) and board[row + i][col + i] == color:
                cnt += 1
                x, y = (row + (row + i)) // 2, (col + (col + i)) // 2
                is_winner(cnt, color, x, y)
            else:
                cnt = 0
                break
        

        for i in range(5):
            if in_range(row + i, col - i) and board[row + i][col - i] == color:
                cnt += 1
                x, y = (row + (row + i)) // 2, (col + (col - i)) // 2
                is_winner(cnt, color, x, y)   
            else:
                cnt = 0
                break
         

print(winner)

        