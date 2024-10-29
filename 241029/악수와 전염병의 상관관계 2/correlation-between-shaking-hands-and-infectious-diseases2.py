# N : 개발자 수
# K : 전염병을 옮기는 횟수
# P : 처음 전염병에 걸린 개발자 번호
# T : 악수 횟수

N, K, P, T = map(int, input().split())

# 개발자 감염여부
developer = [0] * (N+1) # 0:음성 1: 양성
developer[P] = 1

# 악수한 횟수
cnt = [0] * (N+1)

# 악수한 정보
handshake = [list(map(int, input().split())) for _ in range(T)]
handshake.sort(lambda x: x[0])

# t초에 x, y 개발자 악수
for t, x, y in handshake: 
    
    if developer[x] == 1 and developer[y] == 1:
        cnt[x] += 1
        cnt[y] += 1
    elif developer[x] == 1:
        cnt[x] += 1
        if cnt[x] <= K:
            developer[y] = 1
    elif developer[y] == 1:
        cnt[y] += 1
        if cnt[y] <= K:    
            developer[x] = 1
        
    
for n in range(1, N + 1):
    print(developer[n], end="")