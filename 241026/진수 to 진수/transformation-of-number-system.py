a, b = map(int, input().split())
n = list(map(int, list(input())))
n = n[::-1]
num = 0
for i in range(len(n)):
    num = num + a ** i * n[i]

result = []
while True:

    if num < b:
        result.append(num)
        break

    result.append(num % b)
    num = num // b

print(''.join(map(str,result[::-1])))