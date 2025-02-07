n = int(input())
h = [int(input()) for _ in range(n)]

# Write your code here!
result = 0
for i in range(1, max(h)+1):
    cnt = 0
    block = False

    for j in range(n):
        if h[j] > i:
            if block == False:
                cnt += 1
                block = True
        else:
            block=False
    result = max(result, cnt)

print(result)
        