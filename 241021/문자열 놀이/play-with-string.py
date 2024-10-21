s, q = list(input().split())
print(s,q)
for _ in range(int(q)):
    print(_)
    i, a, b = list(input().split())
    print(i, a, b)
    strs = list(s)

    if(i == '1'):
        strs[int(a)-1], strs[int(b)-1] = strs[int(b)-1], strs[int(a)-1]
    else:
        for i in range(len(strs)):
            if(strs[i] == a):
                strs[i] = b
    print(''.join(strs))