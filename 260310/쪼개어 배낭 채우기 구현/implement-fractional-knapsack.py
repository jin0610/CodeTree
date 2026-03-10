N, M = map(int, input().split())    # N개의 보석, 도둑 가방의 크기 M

info = []

for i in range(N):
    w, v = map(int, input().split()) 
    info.append([w, v, v / w])    # 무게(w), 가격(v), 무게 1 당 가격(v / w)

info = sorted(info, key=lambda x : -x[2])

weight, value = 0, 0
for i in range(N):
    if info[i][0] <= M:
        value += info[i][1]
        M -= info[i][0]
    else:
        for j in range(1, info[i][0] + 1):
            if M >= 1:
                value += info[i][2]
                M -= 1
            else:
                break
        break

print(f"{value:.3f}")


