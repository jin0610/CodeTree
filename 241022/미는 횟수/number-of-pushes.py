import sys
A = input()
B = input()

n = 0
while A != B:
    if n >= len(A)-1:
        print(-1)
        sys.exit(0)
    
    B = B[-1]  + B[:-1]
    n = n + 1
print(n)