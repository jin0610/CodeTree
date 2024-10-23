N = int(input())

def sort_(n):

    if n == 0:
        return
    
    print(n, end=" ")
    sort_(n-1)
    print(n, end=" ")

sort_(N)