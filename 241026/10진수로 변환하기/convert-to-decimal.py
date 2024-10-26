digits = list(map(int, list(input())))

digits = digits[::-1]
num = 0
for i in range(len(digits)):
    num = num + 2 ** i * digits[i]

print(num)