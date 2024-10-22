s = input()

strs = ''
for i in s:
    if(i.isdigit() or i.isalpha()):
        strs = strs + i
print(strs.lower())