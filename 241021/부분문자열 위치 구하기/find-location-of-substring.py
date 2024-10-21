import sys
input_str = input()
target_str = input()

input_len, target_len = len(input_str), len(target_str)


for i in range(input_len - target_len):
    is_matched = True
    for j in range(target_len):
        if(target_str[j] != input_str[i+j]):
            is_matched = False
            break
    
    if is_matched:
        print(i)
        sys.exit(0)
    
print(-1)


# if target_str in input_str:
#     result = input_str.index(target_str)
# else:
#     result = -1
         
# print(result)