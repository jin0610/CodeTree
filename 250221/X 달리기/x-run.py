### 케이스 별로 나누기 / X 달리기
X = int(input())

# Write your code here!
pos = 0
speed = 1
time = 0
while pos != X:
    pos += speed
    time += 1

    if (pos >= X // 2):
        if speed == 1:
            speed = 1
        else:
            speed -= 1
    else:
        speed += 1          
    
print(time)
    