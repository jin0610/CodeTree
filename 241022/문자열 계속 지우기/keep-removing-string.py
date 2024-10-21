A = input()
B = input()

while B in A:
    A = A.replace(B,'',1)
print(A)