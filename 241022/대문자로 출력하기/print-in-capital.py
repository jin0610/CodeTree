s = input()

strs =''
for i in s:
    if(i.isalpha()):
        strs = strs + i

print(strs.upper())