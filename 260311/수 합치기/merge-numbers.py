import sys
n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
total_cost = 0
while True:
    arr = sorted(arr, reverse=True)
    cost = arr.pop() + arr.pop()
    arr.append(cost)
    total_cost += cost

    if len(arr) == 1:
        break

print(total_cost)