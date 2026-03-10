n, m = map(int, input().split())

# Note: Using 1-based indexing for words as per C++ code

# Please write your code here.
d = {}
for i in range(n):
    word = input()
    d[word] = i + 1

for i in range(m):
    query = input()
    if query.isdigit():
        print(list(d.keys())[int(query)-1])
    else:
        print(d[query])