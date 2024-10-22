A = input()
B = input()

A_num = ''
B_num =''
for a in A:
    try:
        s = int(a)
        A_num = A_num + str(s)
    except:
        pass

for b in B:
    try:
        s = int(b)
        B_num = B_num + str(s)
    except:
        pass

print(int(A_num) + int(B_num))