### Ad-hoc (고려해야할 대상이 뚜렷해지는 경우) / A, B, C, D 찾기
arr = list(map(int, input().split()))

# Step 1. 오름차순으로 정렬
arr = sorted(arr)

# Step2. 배열의 첫번째(arr[0]), 두번째(arr[1]) 더한 수가 5번째(arr[4])와 같지 않은 경우 D는 다섯번째(arr[4]) 숫자임
if arr[0] + arr[1] != arr[4]:
    print(arr[0], arr[1], arr[2], arr[4])
else:
    print(arr[0], arr[1], arr[2], arr[3])