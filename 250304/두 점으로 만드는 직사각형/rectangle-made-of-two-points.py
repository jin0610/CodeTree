### Ad-hoc (지극히 최선인 전략이 확실히 정해지는 경우) / A, B. C 찾기
arr = list(map(int, input().split()))

# Step 1. 오름차순으로 정렬한다.
arr = sorted(arr)

# Step 2. index 0, 1, 2 더한 값이 -1인 값과 다르면 값 교체
if arr[0] + arr[1] + arr[2] == arr[-1]:
    print(arr[0], arr[1], arr[2])
else:
    print(arr[0], arr[1], arr[3])