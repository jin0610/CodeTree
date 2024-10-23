n1, n2, n3 = list(map(int, input().split()))

def f2(num):
    if num < 10 :
        return num 

    return f2(num//10) + num%10


print(f2(n1 * n2 * n3))