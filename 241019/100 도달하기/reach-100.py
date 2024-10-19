n = int(input())

arr = [1,n]
num = 0
i = 2
while num <= 100:
    num = arr[i-1]+arr[i-2]
    arr.append(num)
    i += 1

for i in range(len(arr)):
    print(arr[i], end = " ")