n = int(input())

color = [[0,0,0] for _ in range(2000)]
start = 1000

for _ in range(n):
    dist, direct = input().split()
    dist = int(dist)
    
    if direct == "R":
        for j in range(0, dist):
            
            if color[start + j][0] == "G":
                pass
            else:
                color[start + j][1] += 1
                if color[start + j][1] >= 2 and color[start + j][2] >= 2:
                    color[start + j][0] = "G"
                else:
                    color[start + j][0] = "B"
        start += (dist - 1)
                
    else:
        for j in range(0, dist):
            
            if color[start - j][0] == "G":
                pass
            else:
                color[start - j][2] += 1
                if color[start - j][1] >= 2 and color[start - j][2] >= 2:
                    color[start - j][0] = "G"
                else:
                    color[start - j][0] = "W"
        start -= (dist - 1)

w, b, g = 0,0,0
for c in color:
    if c[0] == 'W':
        w += 1
    elif c[0] == "B":
        b += 1
    elif c[0] == "G":
        g += 1
    else:
        pass

print(w, b, g)