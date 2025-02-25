### 케이스 별로 나누기 - 좋은 전략 추려내기 / 연속된 숫자 만들기 3
a = list(map(int, input().split()))

# Step 1. list 정렬
a = sorted(a)

# Step 2. 인접한 두 숫자의 간격을 중 더 긴 간격 구하기
max_diff = max(a[2]-a[1], a[1] - a[0])

# Step 3. 더 긴 간격의 -1을 하여 정답 출력
print(max_diff-1)