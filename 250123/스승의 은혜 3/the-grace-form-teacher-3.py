### 물체 단위로 완전탐색 / 스승의 은혜 3
n, b = map(int, input().split())
wishes = [tuple(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    # 학생들이 원하는 선물의 가격 리스트
    tmp = [list(wishes[j]) for j in range(n)]

    # 선물 한 개를 반값 할인
    tmp[i][0] /= 2

    # (선물 가격 + 배송비) 리스트
    prices = [(tmp[k][0] + tmp[k][1]) for k in range(n)]
    prices.sort()

    # 선물할 수 있는 학생수, 현재까지 쓴 예산
    student = 0
    cnt = 0

    for x in range(n):
        if cnt + prices[x] > b:
            break
        cnt += prices[x]
        student += 1

    ans = max(ans, student)

print(ans)