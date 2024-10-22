A = input()
orders = list(input())

for o in orders:
    if o == "L":
        A = A[1:] + A[0]
    else:
        A = A[-1] + A[:-1]

print(A)