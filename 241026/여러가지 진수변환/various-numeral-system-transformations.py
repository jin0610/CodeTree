N, B = map(int, input().split())

result = []

while True:
    if N < B:
        result.append(N)
        break

    result.append(N % B)
    N = N // B

for i in result[::-1]:
    print(i, end="")