n = int(input())

maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

count_map = [[0]*n]*n

count = 0

for i in range(n-1):
    for j in range(n-1):
        if(i == 0 and j == 0):
            
            count_map[i][j] = maps[0][j+1] + maps[i+1][0]
        elif(i == 0):
            count_map[i][j] = maps[0][j+1] + maps[0][j-1] + maps[1][j]
        elif(j == 0):
            count_map[i][j] = maps[i+1][0] + maps[i-1][0] + maps[1][0]
        else:
            count_map[i][j] = maps[i+1][j] + maps[i-1][j] + maps[i][j+1] + maps[i][j-1]

for i in range(n):
    for j in range(n):
        if(count_map[i][j] >= 3):
            count = count + 1

print(count)