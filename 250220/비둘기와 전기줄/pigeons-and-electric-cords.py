### 중간 상황에 대한 예측 / 비둘기와 전기줄
N = int(input())
position = [map(int,input().split()) for _ in range(N)]

# Write your code here!
pis = []
poss = []
cnt = 0
for i in range(N):
    pi, pos = position[i]
    if pi not in pis:
        pis.append(pi)
        poss.append(pos)
    else:
        if poss[pis.index(pi)] != pos:
            cnt += 1
            poss[pis.index(pi)] = pos

print(cnt)