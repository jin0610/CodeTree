X, Y = map(int, input().split())

# Write your code here!
result = 0
for i in range(X, Y+1):
    result = max(result, sum(map(int,str(i))))
print(result)
