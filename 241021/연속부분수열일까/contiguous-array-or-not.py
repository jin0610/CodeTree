n1, n2 = list(map(int, input().split()))

A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = "No"
for i in range(n1-n2+1):
    if result == "Yes":
        break
    
    if( result == "No" and A[i] != B[0]):
        pass
    else:
        for j in range(n2):
            if((A[i+j] == B[j])):
                if(j == n2-1):
                    result = "Yes"
            else:
                break
    
print(result)