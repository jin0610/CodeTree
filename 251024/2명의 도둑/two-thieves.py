N, M, C = map(int, input().split()) # 방 크기(N), 영역 크기(M), 최대 무게(C)
weights = [
    list(map(int, input().split()))
    for _ in range(N)
]

# 선택 가능한 Area
possible_area = []
for r in range(N):
    for c in range(N - M + 1):
        possible_area.append((r, c))

P = N * (N - M + 1) # 선택 가능한 Area 총 갯수

# 무게의 합이 C보다 작으면서 최대 가치를 갖는 조합 찾기
object_combination = [] # 물건 조합
max_value = -1
def find_max_value(depth, cnt, start, area):
    global object_combination, max_value
    if depth == cnt:
        # 무게합 구하기
        value, weight = 0, 0
        for w in object_combination:
            weight += area[w]
            value += area[w] ** 2
        if weight <= C:
            max_value = max(max_value, value)
        return
    
    for m in range(start, M):
        object_combination.append(m)
        find_max_value(depth, cnt + 1, m + 1, area)
        object_combination.pop()

    return

# 가치 구하기
def calc_value(r1, c1, r2, c2):
    global possible_area, max_value
    area1 = weights[r1][c1:c1 + M]
    area2 = weights[r2][c2:c2 + M]

    # 도둑 1이 가질 수 있는 최대 가치 찾기
    max_value = 0
    for m in range(1, M + 1):
        find_max_value(m, 0, 0, area1)
    value1 = max_value

        
    # 도둑2가 가질 수 있는 최대 가치
    max_value = 0
    for m in range(1, M + 1):
        find_max_value(m, 0, 0, area2)
    value2 = max_value

    return value1 + value2

# 겹치는 지 확인
def is_overlap(r1, c1, r2, c2):
    if r1 == r2:
        if c1 > (c2 + M - 1) or c2 > (c1 + M - 1):
            return False
        return True
    else:
        return False
    
answer = -1
for i in range(P):
    r1, c1 = possible_area[i]
    for j in range(i + 1, P):
        r2, c2 = possible_area[j]
        if is_overlap(r1, c1, r2, c2):
            continue
        answer = max(answer, calc_value(r1, c1, r2, c2))

print(answer)