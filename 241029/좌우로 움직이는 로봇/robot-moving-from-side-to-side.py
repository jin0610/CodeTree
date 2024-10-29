n, m = map(int, input().split())

A, B = [0], [0]
a, b = 0, 0

for _ in range(n):
    t, d = input().split()
    t = int(t)

    for i in range(t):
        if d == "R":
            a += 1
        else:
            a -= 1
        A.append(a)

for _ in range(m):
    t, d = input().split()
    t = int(t)

    for i in range(t):
        if d == "R":
            b += 1
        else:
            b -= 1
        B.append(b)

cnt = 0

for i in range(1, max(len(A), len(B))):
    try:
        if A[i] == B[i]:
            if A[i-1] != B[i-1]:
                cnt +=1
    except:
        if len(A) > len(B):
            if A[i] == B[-1]:
                
                cnt +=1
        else:
            if A[-1] == B[i]:
                cnt +=1
print(cnt)