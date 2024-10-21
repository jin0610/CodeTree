A = input()

prev = A[0]
cnt = 1
result = ""

if len(A) == 1:
    result = prev + str(cnt)

for i in range(1,len(A)):
    if(prev == A[i]):
        cnt = cnt + 1
        if i == (len(A) - 1):
            result = result + prev + str(cnt)
    else:
        result = result + prev + str(cnt)

        prev = A[i]
        cnt = 1


print(len(result))
print(result)