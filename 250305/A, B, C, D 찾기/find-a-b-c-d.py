### Ad-hoc (고려해야할 대상이 뚜렷해지는 경우) / A, B, C, D 찾기
arr = list(map(int, input().split()))

# Step 1. 오름차순으로 정렬
arr = sorted(arr)

# Step2. A, B, C, D 찾기
# A + B가 C보다 크거나 작기 때문에 A, B, C는 arr[0] ~ arr[2] 까지임
A, B, C = arr[0], arr[1], arr[2]
D = arr[-1] - (A + B + C)

print(A, B, C, D)