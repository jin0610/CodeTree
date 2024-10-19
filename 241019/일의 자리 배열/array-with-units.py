a, b = list(map(int, input().split()))

result = []
           

for i in range(10):
    if(i == 0):
        result.append(a)
        print(a, end = " ")
    elif(i == 1):
        result.append(b)
        print(b, end = " ")
    else:
        num = result[i-1] + result[i-2]
        num = num%10
        result.append(num)
        print(num, end = " ")