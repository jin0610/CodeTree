### 자리수 단위로 완전탐색 / Carry 피하기 2
import sys

n = int(input())
arr = [int(input()) for _ in range(n)]

# Write your code here!
result = -sys.maxsize
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            carry = 0
            num1, num2, num3 = arr[i], arr[j], arr[k]
            while ((num1 % 10) + (num2 % 10) + (num3 % 10)) != 0:
                if ((num1 % 10) + (num2 % 10) + (num3 % 10)) > 10:
                    carry = 1
                    break
                else:
                    num1, num2, num3 = num1 // 10, num2 // 10, num3 // 10
            if carry == 0:
                num = arr[i] + arr[j] + arr[k]
                result = max(result, num)

print(result)

