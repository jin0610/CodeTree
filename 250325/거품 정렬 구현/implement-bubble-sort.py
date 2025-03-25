n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

while True:
    isSort = False

    if isSort:
        break
    
    for i in range(n-1):
        isSort = True
        if arr[i] > arr[i + 1]:
            isSort = False
            arr[i], arr[i+1] = arr[i+1], arr[i]

print(' '.join(arr))