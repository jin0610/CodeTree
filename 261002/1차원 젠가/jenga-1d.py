n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

def remove_block(s, e, arr):
    temp = []
    for i in range(len(arr)):
        if s <= i <= e:
            continue
        temp.append(arr[i])
    return temp

arr = remove_block(s1 - 1, e1 - 1, arr)
arr = remove_block(s2 - 1, e2 - 1, arr)

print(len(arr))
for i in range(len(arr)):
    print(arr[i])
