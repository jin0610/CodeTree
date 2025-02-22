### 케이스 별로 나누기 / X 달리기
X = int(input())

# Write your code here!
pos = 0
speed = 1
time = 0
while True:
    pos += speed    # 현재 속도로 이동
    time += 1       # 시간 1 증가
    speed += 1      # 속도 증가
    if pos == X:
        break

    ## 속도 1증가했을 때
    speed_increase = 0
    for i in range(speed):
        speed_increase += i
    
    # 다음 위치가 목표 지점을 초과할 경우 속도 감소
    if (X - (pos + speed) < speed_increase):
        speed -= 1

    ## 현재 속도로 정지할 경우 거리 계산
    stay_speed = 0
    for i in range(speed):
        stay_speed += i
    
    # 다음 위치가 목표 지점을 초과할 경우 속도 감소
    if (X - (pos + speed) < stay_speed):
        speed -= 1
    
    
print(time)
    