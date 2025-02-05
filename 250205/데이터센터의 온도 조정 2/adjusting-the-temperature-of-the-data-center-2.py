### 탐색 범위가 불명확한 경우에 대한 완전 탐색 / 데이터 센터의 온도 조정 2
N, C, G, H = map(int, input().split())

# Write your code here!
works = [0] * 1001
for i in range(N):
    Ta, Tb = map(int, input().split())
    for j in range(Ta):
        works[j] += C
    
    for j in range(Ta, Tb + 1):
        works[j] += G

    for j in range(Tb+1, 1001):
        works[j] += H

print(max(works))
