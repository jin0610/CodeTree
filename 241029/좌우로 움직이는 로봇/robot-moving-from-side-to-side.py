n,m = map(int, input().split())

A = [0]
B = [0]
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


cnt = 1
for i in range(1, min(len(A),len(B))):
    if B[i] == A[i]:
        if B[i-1] != A[i-1]:
            cnt += 1
    else:
        pass
print(cnt)