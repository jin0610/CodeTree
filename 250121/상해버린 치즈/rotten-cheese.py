### 물체 단위로 완전탐색 / 상해버린 치즈
N, M, D, S = map(int, input().split())
info = [tuple(map(int, input().split())) for _ in range(D)] # (p, m, t) : (몇 번째 사람(p), 몇 번째 치즈(m), 언제먹었는지(t초))
sick = [tuple(map(int, input().split())) for _ in range(S)] # (p, t) : (몇 번째 사람(p),언제 아팠는지(t초))
info = sorted(info, key = lambda x : x[-1])
sick = sorted(sick, key = lambda x : x[-1])

sick_p = []
cheese = []

for i in range(S):
    sp, st = sick[i]
    for j in range(D):
        dp, dm, dt = info[j]
        if sp == dp:
            cheese.append(dm)
        if dm in cheese or st > dt:
            sick_p.append(dp)

medicine_cnt = len(set(sick_p))
print(medicine_cnt)
