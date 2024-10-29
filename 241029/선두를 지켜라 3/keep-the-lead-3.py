N, M = map(int, input().split())

A, B = [0],[0]
a, b = 0,0

for _  in range(N):
    v, t = map(int, input().split())
    for i in range(t):
        a += v
        A.append(a)

for _  in range(M):
    v, t = map(int, input().split())
    for i in range(t):
        b += v
        B.append(b)

honer = ""
cnt = 0

for i in range(len(A)):
    if A[i] > B[i]:
        if honer != 'A':
            cnt += 1
            honer = 'A'
    elif A[i] < B[i]:
        if honer != 'B':
            cnt += 1
            honer = 'B'
    else:
        if honer != 'AB':
            cnt += 1
            honer = 'AB'
        
print(cnt - 1)