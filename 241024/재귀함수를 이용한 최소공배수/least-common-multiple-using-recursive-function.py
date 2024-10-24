n = int(input())

nums = list(map(int, input().split()))

# 최대공약수
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

# 최소 공배수
def lcm(a, b):
    return a * b // gcd(a, b)

def cal(arr):
    if len(arr) == 1:
        return arr[0]

    elif len(arr) == 2:
        return lcm(arr[0], arr[1])

    else:
        return lcm(arr[0], cal(arr[1:]))

print(cal(nums))