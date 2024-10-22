A = input()

result = 0
for a in A:
    if(a.isdigit()):
        result = result + int(a)
print(result)