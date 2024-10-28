N, M = map(int, input().split())

a_arr, b_arr = [0], [0]
a, b = 0, 0
for n in range(N):
    v, t = map(int, input().split())

    for i in range(t):
        a += v
        a_arr.append(a)

for m in range(M):
    v, t = map(int, input().split())

    for i in range(t):
        b += v
        b_arr.append(b)

cnt = 0
sign_1 = 0
for i in range(1, len(a_arr)):
    diff = a_arr[i] - b_arr[i]
    if diff > 0:
        sign_2 = 1
        if sign_2 != sign_1:
            sign_1 = sign_2
            cnt += 1

    elif diff < 0:
        sign_2 = -1
        if sign_2 != sign_1:
            sign_1 = sign_2
            cnt += 1
    else:
        pass
print(cnt-1)