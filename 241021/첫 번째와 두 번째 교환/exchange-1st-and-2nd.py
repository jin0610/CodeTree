s = list(input())

_1 = s[0]
_2 = s[1]

result=[]

for i in s:
    if(i == _1):
        result.append(_2)
    elif(i == _2):
        result.append(_1)
    else:
        result.append(i)

print(''.join(result))