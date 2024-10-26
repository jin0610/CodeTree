N, K = map(int, input().split())

block = [0] * N
for k in range(K):
    a, b = map(int, input().split())
    
    if a == b:
        block[a-1] = block[a-1] + 1
    else:
        for i in range(a-1, b):
            block[i] = block[i] + 1 
        

print(max(block))