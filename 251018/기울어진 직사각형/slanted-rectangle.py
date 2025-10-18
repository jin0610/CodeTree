def in_range(x, y):
    return x >= 0 and x < N and y >= 0 and y < N

def calculate(x, y, w, h):
    move_cnt = [w, h, w, h]
    num = 0
    for dx, dy, length in zip(dxs, dys, move_cnt):
        for _ in range(length):
            x += dx
            y += dy

            if not in_range(x, y):
                return 0
            
            num += grid[y][x]

    return num
        
if __name__ == '__main__':
    N = int(input())
    grid = [
        list(map(int,input().split()))
        for _ in range(N)
    ]

    dxs = [1, -1, -1, 1]
    dys = [-1, -1, 1, 1]
    answer = 0

    for i in range(N):
        for j in range(N):
            for w in range(1, N):
                for h in range(1, N):
                    answer = max(answer, calculate(j, i, w, h))

    print(answer)