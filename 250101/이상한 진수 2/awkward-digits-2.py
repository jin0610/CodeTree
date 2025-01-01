### 자리 수 단위로 완전탐색 / 이상한 진수2

a = input()

result = -1

for i in range(len(a)):

    ## if문을 사용하지 않은 풀이 44ms
    num = a[:i] + str(1 - int(a[i])) + a[i+1:]

    ## if문을 사용하는 풀이 43ms
    # if a[i] == '1':
    #     num = a[:i] + '0' + a[i+1:]
    # else:
    #     num = a[:i] + '1' + a[i+1:]

    result = max(result, int(num,2))  

print(result)
        
