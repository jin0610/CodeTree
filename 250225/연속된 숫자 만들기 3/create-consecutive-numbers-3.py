### 케이스 별로 나누기 - 좋은 전략 추려내기 / 연속된 숫자 만들기 3
a = list(map(int, input().split()))

a = sorted(a)

max_diff = max(a[2]-a[1], a[1] - a[0])
print(max_diff-1)