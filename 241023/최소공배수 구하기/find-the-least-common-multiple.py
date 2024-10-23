n, m = map(int,input().split())

def min_(a,b):
    while b > 0:
        a, b = b, a % b
    return a

result = (n * m) // min_(n, m)

print(result)