N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

def solution(arr):
    N = len(arr)
    arr2 = [[0]*(N-2) for _ in range(N)]
    
    if(N == 3):
        arr2[0][0] = sum(arr[0]) + sum(arr[1]) + sum(arr[2])
        return arr2[0][0]

    max_cnt = 0
    for i in range(N-2):
        for j in range(N-2):
            arr2[i][j] = sum(arr[i]) + sum(arr[i+1]) +sum(arr[i+2])
            max_cnt = max(arr2[i][j], max_cnt)

    return max_cnt

print(solution(arr))