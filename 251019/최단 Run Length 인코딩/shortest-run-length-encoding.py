import sys

A = input()
list_A = list(A)

def shift():
    temp = list_A[-1]
    for i in range(len(list_A) - 1, 0 , -1):
        list_A[i] = list_A[i - 1]
    list_A[0] = temp

def RunLengthEncoding(str_list):
    temp_str = ""
    cnt, s = 1, str_list[0]
    for i in range(len(str_list)):
        if str_list[i] == s:
            cnt += 1
        else:
            temp_str = temp_str + s + str(cnt)
            cnt, s = 1, str_list[i]
    temp_str = temp_str + s + str(cnt)
    return len(temp_str)

answer = sys.maxsize
while True:
    shift()
    answer = min(answer, RunLengthEncoding(list_A))
    if list_A == list(A):
        break
print(answer)
