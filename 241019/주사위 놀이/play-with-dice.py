arr = list(map(int, input().split()))

result = [0]*6
for i in range(10):
    result[arr[i]-1] +=1

for i in range(6):
    print(f"{str(i + 1)} - {str(result[i])}")