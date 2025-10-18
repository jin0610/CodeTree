A = input()

def RunLengthEncoding(strs):
    temp_str = ""
    cnt, s = 1, strs[0]
    for i in range(len(strs)):
        if strs[i] == s:
            cnt += 1
        else:
            temp_str = temp_str + s + str(cnt)
            cnt, s = 1, strs[i]
    temp_str = temp_str + s + str(cnt)
    return len(temp_str)

answer = RunLengthEncoding(A)
B = A[:]
while True:
    B = B[-1] + B[:-1]
    answer = min(answer, RunLengthEncoding(B))
    if B == A:
        break
print(answer)