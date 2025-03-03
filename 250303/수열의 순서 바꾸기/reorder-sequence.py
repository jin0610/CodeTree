### Ad-hoc (지극히 최선인 전략이 확실히 정해지는 경우) / 수열의 순서 바꾸기
n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.
if n == 1:
    print(0)
else:
    answer = 0
    for i in range(n - 2, -1, -1):
        if sequence[i] > sequence[i + 1]:
            answer += i + 1
            break
    print(answer)