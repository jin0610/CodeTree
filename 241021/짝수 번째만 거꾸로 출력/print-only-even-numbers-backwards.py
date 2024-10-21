strs = input()

result = ""
for i in range(len(strs)):
    if(i % 2 == 1):
        result += strs[i]

print(result[::-1])