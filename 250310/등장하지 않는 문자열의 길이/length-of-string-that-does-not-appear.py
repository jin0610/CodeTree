### 완전탐색 (상황을 일일이 가정해보고 진행하는 완전탐색) / 등장하지 않는 문자열의 길이
n = int(input())
strs = input()

# Write your code here!
str_len = 1
while True:
    check = False
    for i in range(n - str_len):
        tmp = strs[i : i + str_len]
        if strs.count(tmp) >= 2:
            check = True   
            break
    if check == False:
        print(str_len)
        break
    else:
        str_len += 1
