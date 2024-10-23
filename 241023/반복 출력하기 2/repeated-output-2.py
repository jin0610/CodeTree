n = int(input())

def helloworld(n):
    
    if n == 0:
        return

    print("HelloWorld")
    helloworld(n-1)

helloworld(n)