n = int(input())

d = {}
for i in range(n):
    word = input()
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

print(max(d.values()))