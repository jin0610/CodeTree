from sortedcontainers import SortedDict

n = int(input())
sd = SortedDict()

for i in range(n):
    command = input().split()
    c = command[0]

    if c == "add":
        k = int(command[1])
        sd[k] = command[2]
    elif c == "remove":
        k = int(command[1])
        if k in sd:
            sd.pop(k)
    elif c == "find":
        k = int(command[1])
        if k in sd:
            print(sd[k])
        else:
            print(None)
    else:
        if sd:
            print(*sd.values())
        else:
            print("None")
    # print(sd) # 디버깅용