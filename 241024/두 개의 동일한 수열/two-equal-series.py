n = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

if A.sort() == B.sort():
    print("Yes")
else:
    print('No')