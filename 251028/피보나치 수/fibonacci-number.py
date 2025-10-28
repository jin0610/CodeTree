N = int(input())

def fibbo(n):
    if n == 1 or n == 2:
        return 1
    
    return fibbo(n-1) + fibbo(n-2)

print(fibbo(N))