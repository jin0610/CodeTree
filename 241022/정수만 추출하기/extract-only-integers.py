a, b = input().split()

a2, b2 = '', ''
for i in a:
    try:
        s = int(i)
        a2 = a2 + str(s)        
    except:
        break

for i in b:
    try:
        s=int(i)
        b2 = b2 + str(s)
    except:
        break
print(int(a2) + int(b2))