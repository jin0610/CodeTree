### 완전탐색 / 초기 수열 복원하기
N = int(input())
arr = list(map(int, input().split()))

for i in range(1, N + 1):
    answer = [0] * N
    flag = True
    answer[0] = i
    for j in range(N-1):
        num = arr[j] - answer[j]
        if (num <= 0) or (num > N) or (num in answer):
            flag = False
            break
        answer[j + 1] = num
    
    if flag:
        print(" ".join(map(str,answer)))
        break
        

    
