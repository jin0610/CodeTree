n = int(input())

s = set()
for i in range(n):
    c, x = input().split()

    if c == "add":
        s.add(x)
    elif c == "remove":
        s.remove(x)
    else:
        if x in s:
            print("true")
        else:
            print("false")
    

# Please write your code here.
