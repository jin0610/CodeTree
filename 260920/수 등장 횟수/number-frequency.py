N, M = map(int, input().split())
arr1 = list(map(int, input().split()))

num_dict = dict()
for n in arr1:
    if n in num_dict.keys():
        num_dict[n] += 1
    else:
        num_dict[n] = 1

arr2 = list(map(int, input().split()))
for m in arr2:
    if m in num_dict.keys():
        print(num_dict[m], end=' ')
    else:
        print(0, end=' ')