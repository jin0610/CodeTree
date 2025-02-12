n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# Write your code here!
answer = 0
for i in range(n + 1):
    temp = 0
    idx = i
    for j in range(m):
        temp += arr[idx]
        idx = arr[idx]
    answer = max(answer, temp)
print(answer)
