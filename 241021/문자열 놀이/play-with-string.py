strs, q = list(input().split())

strs = list(strs)

for _ in range(int(q)):
    i, a, b = list(input().split())

    if(i == '1'):
        strs[int(a)-1], strs[int(b)-1] = strs[int(b)-1], strs[int(a)-1]
    else:
        for i in range(len(strs)):
            if(strs[i] == a):
                strs[i] = b
    print(''.join(strs))