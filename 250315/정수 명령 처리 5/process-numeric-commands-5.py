N = int(input())

arr = []
for _ in range(N):
    command = input().split()
    
    if command[0] == "push_back":
        num = int(command[1])
        arr.append(num)
    elif command[0] == "pop_back":
        arr.pop()
    elif command[0] == "size":
        print(len(arr))
    else:
        num = int(command[1])
        print(arr[num-1])

