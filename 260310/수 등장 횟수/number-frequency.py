n, m = map(int, input().split())    # 원소의 개수 n, 질의의 수 m
arr = list(map(int, input().split()))
nums = list(map(int, input().split()))

# Please write your code here.
num_to_index = {}

for i, elem in enumerate(arr):
    if elem in num_to_index:
        num_to_index[elem] += 1
    else:
        num_to_index[elem] = 1
    
for n in nums:
    if n in num_to_index:
        print(num_to_index[n], end=" ")
    else: 
        print(0, end=" ")