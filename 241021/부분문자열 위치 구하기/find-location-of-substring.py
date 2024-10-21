input_str = input()

target_str = input()
result = 0
for i in range(len(input_str)-len(target_str)):
    if target_str in input_str:
        result = input_str.index(target_str)
    else:
        result = -1
         
print(result)