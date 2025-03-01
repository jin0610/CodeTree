### 케이스 별로 나누기 (가능한 상황을 나열하기) / 세 수의 최대의 곱
n = int(input())
arr = list(map(int, input().split()))

arr = sorted(arr)

# Case 1. 가장 큰 양수 3개 곱하기
num1 = arr[-1] * arr[-2] * arr[-3]

# Case 2. 가장 큰 양수 1개, 가장 작은 음수 2개 곱하기
num2 = arr[0] * arr[1] * arr[-1]

# 두 수중 큰 숫자
print(max(num1, num2))

