### 자리수 단위로 완전탐색 / 오목
import sys
board = [list(map(int, input().split())) for _ in range(19)]

# Write your code here!
winner = 0
for row in range(14):
    for col in range(14):
        if board[row][col] == 0:
            continue
        else:
            color = board[row][col]
            # 가로줄 비교
            colors = board[row][col:col+5]
            if len(set(colors)) == 1:
                print(color)
                print(row + 1 , col + 3)
                sys.exit()

            # 세로줄 비교           
            colors = [board[row+i][col] for i in range(5)]
            if len(set(colors)) == 1:
                print(color)
                print(row + 3, col + 1)
                sys.exit()

            # 대각선 비교
            colors = [board[row+i][col+i] for i in range(5)]
            if len(set(colors)) == 1:
                print(color)
                print(row + 3, col + 3)
                sys.exit()

            if col >= 4:
                colors = [board[row+i][col-i] for i in range(5)]
                if len(set(colors)) == 1:
                    print(color)
                    print(row + 3, col - 1)
                    sys.exit()

print(winner)
