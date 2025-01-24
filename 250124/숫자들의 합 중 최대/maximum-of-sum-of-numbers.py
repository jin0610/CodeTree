X, Y = map(int, input().split())

# Write your code here!
result = 0
## 재귀
def digit_sum(n):
    if n < 10:
        return n
    else:
        return digit_sum(n // 10) + (n % 10)

for i in range(X, Y + 1):
    result = max(result, digit_sum(i))
# for i in range(X, Y+1):
    # result = max(result, sum(map(int,str(i))))
print(result)

