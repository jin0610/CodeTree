A = input()

dic = {}

prev = A[0]
cnt = 1
result = ""

for i in range(1,len(A)):

    if(prev == A[i]):
        cnt += 1
    else:
        result += prev
        result += str(cnt)

        prev = A[i]
        cnt = 1
    if(i == len(A)-1):
        result += prev
        result += str(cnt)

print(len(A))
print(result)