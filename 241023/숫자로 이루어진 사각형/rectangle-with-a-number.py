N = int(input())

num = 1

def rect(n):
    num = 1
    for i in range(n):
        for j in range(n):
            print(num, end=" ")
        
            if(num == 9):
                num = 1
            else:
                num = num + 1
        print()

rect(N)