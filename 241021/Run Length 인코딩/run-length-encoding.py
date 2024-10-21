A = input()

prev = A[0]
cnt = 1
result = ""

for i in range(1,len(A)):
    if(prev == A[i]):
        cnt = cnt + 1
        
    else:
        result = result + prev + str(cnt)

        prev = A[i]
        cnt = 1

result = result + prev + str(cnt)

print(len(result))
print(result)