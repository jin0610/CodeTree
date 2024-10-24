n =int(input())

nums = list(map(int, input().split()))

for i in range(1, n + 1, 2):
    arr = nums[:i]
    arr.sort()

    print(arr[(i-1)//2], end=" ")