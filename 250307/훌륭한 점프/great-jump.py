### 완전탐색 / 훌륭한 점프
N, K = map(int, input().split())
stone = list(map(int,input().split()))

def is_possible(max_val):
    available_indices = []
    for i, elem in enumerate(stone):
        if elem <= max_val:
            available_indices.append(i)

    arr_size = len(available_indices)
    for i in range(1, arr_size):
        dist = available_indices[i] - available_indices[i-1]
        if dist > K:
            return False
    
    return True

answer = 0
for i in range(1, N):
    if is_possible(i):
        answer = max(answer, i)
        
print(answer)