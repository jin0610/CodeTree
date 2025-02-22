### 케이스 별로 나누기 / X 달리기
X = int(input())

# Write your code here!
pos = 0
speed = 1
time = 0
while True:
    pos += speed
    time += 1
    re_dist = X - pos

    if re_dist <= 0:
        break

    if (pos >=  X // 2):
        if re_dist >= speed * 2 or speed == 1:
            continue
        else:
            speed -= 1
    else:
        speed += 1
    
print(time)
    