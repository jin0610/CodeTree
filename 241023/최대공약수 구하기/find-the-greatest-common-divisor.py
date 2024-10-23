def maxnum(n,m):
    num = []
    for i in range(1, min(n,m)+1):
        if(n % i == 0 and m % i == 0):
            num.append(i)
    return max(num)

n, m = map(int, input().split())

print(maxnum(n,m))