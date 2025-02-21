### 케이스별로 나누기(일어난 상황에 대한 추론) / 달리자
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Write your code here!
dist = 0
for i in range(n):
    move = 0
    if A[i] > B[i]:
        move = A[i] - B[i]
        dist = dist + move
        if move > 0:
            A[i + 1] += move

print(dist)
 