arr = []
total = 0
for i in range(2):
    nums = list(map(int, input().split()))
    print(round(sum(nums)/4,1 ), end= " ")
    total += sum(nums)
    arr.append(nums)
print()

arr2 = list(zip(*arr))
for i in range(4):
    print(round(sum(arr2[i])/2, 1), end = " ")
print()

print(round(total/8,1))