n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(n-1):
    minimum = arr.index(min(arr[i:n]))
    arr[i], arr[minimum] = arr[minimum], arr[i]

print(*arr)
