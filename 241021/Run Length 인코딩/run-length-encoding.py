A = input()

dic = {}

prev = A[0]
cnt = 1
result = A[0]+str(cnt)

for i in range(1,len(A)):
    if(prev == A[i]):
        cnt = int(result[-1]) + 1
        result = result[:-1] + str(cnt)
    else:
        prev = A[i]
        cnt = 1
        result = result + prev + str(cnt)

print(len(result))
print(result)