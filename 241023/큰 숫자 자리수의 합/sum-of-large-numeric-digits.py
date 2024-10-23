nums = list(map(int, input().split()))

num = 1

def f2(num):
    if num < 10 :
        return num 

    return f2(num//10) + num%10

for i in range(3):
    num = num * nums[i]

print(f2(num))