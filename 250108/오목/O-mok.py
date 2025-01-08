### 자리 수 단위로 완전탐색 / 오목
import sys
board = [list(map(int, input().split())) for _ in range(19)]

# Write your code here!

def in_range(x, y):
    return x >= 0 and x < 19 and y >= 0 and y < 19

# 8방위[NW, N, NE, E, ES, S, SW, W]
dxs, dys= [-1, 0, 1, 1, 1, 0, -1, -1], [-1, -1, -1, 0, 1, 1, 1, 0]

winner = 0

for x in range(19):
    for y in range(19):

        if board[x][y] == 0:
            continue

        color = board[x][y]

        for i in range(4):
            dx1, dy1 = x + dxs[i], y + dys[i]
            dx2, dy2 = x + dxs[i + 4], y + dys[i + 4]
            if in_range(dx1, dy1) and in_range(dx2, dy2) and board[dx1][dy1] == color and board[dx2][dy2] == color:
                dx1, dy1 = x + 2*dxs[i], y + 2*dys[i]
                dx2, dy2 = x + 2*dxs[i + 4], y + 2*dys[i + 4]
                if in_range(dx1, dy1) and in_range(dx2, dy2) and board[dx1][dy1] == color and board[dx2][dy2] == color:
                    print(color)
                    print(x + 1, y + 1)
                    sys.exit(0)
            else:
                continue

print(winner)
