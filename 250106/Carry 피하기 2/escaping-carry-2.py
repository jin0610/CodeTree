### 자리수 단위로 완전탐색 / Carry 피하기 2
import sys

n = int(input())
arr = [int(input()) for _ in range(n)]

# Write your code here!
result = -sys.maxsize
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            carry = False
            num1, num2, num3 = arr[i], arr[j], arr[k]
            sum_re = (num1 % 10) + (num2 % 10) + (num3 % 10)
            while (num1 > 0 or num2 > 0 or num3 > 0) and carry == False:
                if sum_re >= 10:
                    carry = True
                else:
                    num1, num2, num3 = num1 // 10, num2 // 10, num3 // 10
                    sum_re = (num1 % 10) + (num2 % 10) + (num3 % 10)
            
            if carry == False:
                num = arr[i] + arr[j] + arr[k]
                result = max(result, num)
                

if result < 0:
    print(-1)
else:
    
    print(result)

