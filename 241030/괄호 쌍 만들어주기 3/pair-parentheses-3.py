arr = list(input())

cnt = 0
for i in range(len(arr)):
    if arr[i] == "(":
        for j in range(i, len(arr)):
            if j != i and arr[j] == ")":
                cnt += 1

    else:
        pass

print(cnt)