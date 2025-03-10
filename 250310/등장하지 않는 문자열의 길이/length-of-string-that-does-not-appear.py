### 완전탐색 (상황을 일일이 가정해보고 진행하는 완전탐색) / 등장하지 않는 문자열의 길이
n = int(input())
strs = input()

# Write your code here!
str_len = 1
while True:
    check = False
    for i in range(n - str_len + 1):
        tmp = strs[i : i + str_len]
        cnt = 0
        for j in range(n - str_len + 1):
            tmp2 = strs[j : j + str_len]
            if tmp == tmp2:
                cnt += 1
                if cnt >= 2:
                    check = True
                    break
        
        if check == True:
            break
        
    if check == False:
        break
    else:
        str_len += 1
print(str_len)