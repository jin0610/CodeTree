A = input()

for a in A:
    if a.islower():
        print(a.upper(), end="")
    else:
        print(a.lower(),end="")