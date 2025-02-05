X, Y = map(int, input().split())

# Write your code here!
result = 0
for num in range(X, Y+1):
    num_list = list(map(int, str(num)))
    if len(set(num_list)) == 2:
        number = list(set(num_list))
        if num_list.count(number[0]) == 1 or num_list.count(number[1]) == 1:
            result += 1

print(result)
