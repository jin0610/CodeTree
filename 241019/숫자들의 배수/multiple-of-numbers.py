n = int(input())

cnt = 0
i = 1
while cnt != 2:
    num = n * i
    print(num, end = " ")
    if(num % 5 == 0):
        cnt += 1
    i += 1