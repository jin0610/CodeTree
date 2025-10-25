import sys
INT_MAX = sys.maxsize
n = int(input())
grid = [list(input()) for _ in range(n)]

# 시작점, 끝점, 동전 찾기
coins_pos = {}
coins = []
for r in range(n):
    for c in range(n):
        if grid[r][c] == 'S':
            start = (r, c)
        elif grid[r][c] == 'E':
            end = (r, c)
        elif grid[r][c] == '.':
            continue
        else:
            coins_pos[grid[r][c]] = (r, c)
            coins.append(grid[r][c])
coins = sorted(coins)

# 최소 3개의 동전을 수집해 도착지에 도달하기 위해 필요한 최소한 이동 횟수
def get_dist(coins):
    global coins_pos, start, end
    dist = 0
    # start -> coins[0]
    coin1 = coins_pos[coins[0]]
    dist += (abs(start[0] - coin1[0]) + abs(start[1] - coin1[1]))

    # coins간 이동
    for i in range(2):
        coin1 = coins_pos[coins[i]]
        coin2 = coins_pos[coins[i + 1]]

        dist += (abs(coin1[0] - coin2[0]) + abs(coin1[1] - coin2[1]))

    # coins -> end
    coin1 = coins_pos[coins[-1]]
    dist += (abs(end[0] - coin1[0]) + abs(end[1] - coin1[1]))

    return dist

answer = INT_MAX
coin_comb = []
def get_min_move(curr_idx, cnt):
    global answer, coins, coin_comb

    # 종료조건 : 3개의 동전 고르기
    if cnt == 3:
        answer = min(answer, get_dist(coin_comb))
        return

    # 동전이 모자란 경우 
    # 1. 격자 안에 동전의 갯수가 3개 미만인 경우 len(coins) < 3
    if len(coins) < 3:
        return

    for i in range(curr_idx, len(coins)):
        coin_comb.append(coins[i])
        get_min_move(i + 1, cnt + 1)
        coin_comb.pop()

    return

get_min_move(0, 0)

if answer == INT_MAX:
    print(-1)
else:
    print(answer)