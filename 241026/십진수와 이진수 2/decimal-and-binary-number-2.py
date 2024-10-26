N = list(map(int,list(input())))

N = N[::-1]
digit = 0
for i in range(len(N)):
    digit = digit + 2 ** i * N[i]

digit  = digit * 17
digits = []

while True:
    if digit < 2:
        digits.insert(0, digit)
        break
    
    digits.insert(0, digit % 2)
    digit = digit // 2

print(''.join(map(str, digits)))