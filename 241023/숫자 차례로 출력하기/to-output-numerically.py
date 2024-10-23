N = int(input())

def _print(n):
    if n==0:
        return

    _print(n-1)
    print(n, end=' ')  

def _print2(n):
    if n==0:
        return

    print(n, end=' ')  
    _print2(n-1)
    
_print(N)
print()
_print2(N)