import sys

N, M = map(int, input().split())

A, B = [0],[0]
a, b = 0, 0

for _ in range(N):
    d, t = input().split()
    t = int(t)

    for i in range(t):
        if d == "R":
            a += 1
        else:
            a -= 1
        A.append(a)

for _ in range(M):
    d, t = input().split()
    t = int(t)

    for i in range(t):
        if d == "R":
            b += 1
        else:
            b -= 1
        B.append(b)

for i in range(1, len(A)):
    if A[i] == B[i]:
        print(i)
        sys.exit(0)

print(-1)