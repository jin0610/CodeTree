n = int(input())

strs = input().replace(" ",'')
for i in range(len(strs)):
    print(strs[i],end='')
    if (i + 1) % 5 == 0:
        print()