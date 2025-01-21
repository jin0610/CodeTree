### 물체 단위로 완전탐색 / 개발자의 순위
K, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(K)]

# Write your code here!
cnt = 0
for i in range(N):
    
    for j in range(N):
        flag = True
        if i == j:
            continue
        for a in arr:
            idx_i, idx_j = a.index(i+1), a.index(j+1)
            if idx_i > idx_j:
                flag = False                

        if flag == True:
            cnt += 1

print(cnt)

