### 정보에 따른 숫자 2
T, a, b = map(int, input().split())
alpha = [tuple(input().split()) for _ in range(T)]

cnt = 0
for i in range(a, b + 1):
    d1, d2 = 1000,1000
    for char, idx in alpha:
        idx = int(idx)
        if char == 'S':
            d1 = min(d1, abs(i-idx))
        if char == 'N':
            d2 = min(d2, abs(i-idx))

    if d1 <= d2:
        cnt += 1

    
    
print(cnt)