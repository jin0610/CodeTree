### 자리 수 단위로 완전탐색 / 이상한 진수2

a = input()

N = int(a, 2)

for i in range(len(a)):
    if a[i] == '1':
        num = a[:i] + '0' + a[i+1:]
        
    else:
        num = a[:i] + '1' + a[i+1:]

    N = max(N, int(num,2))  

print(N)
        
