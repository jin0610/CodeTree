a, b = list(map(int, input().split()))

re = [0] * b
while a > 1:
    idx = (a % b)
    re[idx] += 1
    a = a // b

re = [n * n for n in re]
print(sum(re))