strs = list(input())
x, y = 0, 0
curr_dir = 3

# 동 남 서 북
dxs = [1, 0, -1 , 0]
dys = [0, -1, 0, 1]

for i in range(len(strs)):
    # 왼쪽(반시계방향)
    if(strs[i] == "L"):
        curr_dir = (curr_dir - 1 + 4) % 4
    # 오른쪽(시계방향)
    elif(strs[i] == "R"):
        curr_dir = (curr_dir + 1 + 4) % 4
    else:
        x, y = x + dxs[curr_dir], y + dys[curr_dir]

print(x,y)