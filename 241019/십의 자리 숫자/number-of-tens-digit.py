nums = list(map(int, input().split()))

result = [0]*10
for num in nums:
    if(num == 0):
        break
    else:
        result[num // 10] += 1

for i in range(1, 10):
    print(f"{str(i)} - {str(result[i])}")