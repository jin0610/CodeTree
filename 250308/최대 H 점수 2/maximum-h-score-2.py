### 완전탐색 3 (기준을 새로 설정하여 완전탐색) / 최대 H 점수 2
N, L = map(int, input().split())
seq = list(map(int, input().split()))


for h in range(N, -1, -1):
    l_cnt, h_cnt = 0, 0
    for i in range(N):
        if seq[i] >= h:
            h_cnt += 1
        elif seq[i] == h - 1:
            h_cnt += 1
            l_cnt += 1
    if h_cnt >= h and (l_cnt-(h_cnt - h)) <= L:
        print(h)
        break   