### 정보에 따른 숫자 2
T, a, b = map(int, input().split())

alpha = [0] * (1001)
for t in range(T):
    char, idx = input().split()
    if char == "N":
        alpha[int(idx)] = "N"
    else:
        alpha[int(idx)] = "S"

cnt = 0
for i in range(a, b + 1):
    d1, d2 = 1000,1000
    for j in range(1, 1001):
        if alpha[j] == 'S':
            d1 = min(d1, abs(j-i))
        if alpha[j] == 'N':
            d2 = min(d2, abs(j-i))

    if d1 <= d2:
        cnt += 1

    
    
print(cnt)