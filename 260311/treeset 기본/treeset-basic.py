from sortedcontainers import SortedSet

n = int(input())

s = SortedSet()

for _ in range(n):
    commands = input().split()
    c = commands[0]

    if  c == "add":
        x = int(commands[1])
        s.add(x)
    elif c == "remove":
        x = int(commands[1])
        s.remove(x)
    elif c == "find":
        x = int(commands[1])
        if x in s:
            print("true")
        else:
            print("false")
    elif c =="lower_bound":
        x = int(commands[1])
        idx = s.bisect_left(x)
        try:       
            print(s[idx])
        except:
            print("None")
    elif c =="upper_bound":
        x = int(commands[1])
        idx = s.bisect_right(x)
        try:       
            print(s[idx])
        except:
            print("None")
    elif c == "largest":
        if s:
            print(s[-1])
        else:
            print("None")
    else:
        if s:
            print(s[0])
        else:
            print("None")
