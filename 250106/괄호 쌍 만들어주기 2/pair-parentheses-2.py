### 자리수 단위로 완전탐색 / 괄호 쌍 만들어주기2
A = input()

# Write your code here!
result = 0

for i in range(len(A)-1):
    if A[i] == '(' and A[i+1] == '(':
        for j in range(i+2,len(A)-1):
            if A[j] == ')' and A[j+1] == ')':
                result += 1

print(result)

