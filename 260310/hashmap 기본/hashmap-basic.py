n = int(input())

answer = dict()
for i in range(n):
    commands = input().split()
    c, k = commands[0], commands[1]
    if c == "add":
        answer[k] = commands[2]
    elif c == "remove":
        if k in answer:
            answer.pop(k)
    else:
        if k in answer:
            print(answer[k])
        else:
            print(None)
