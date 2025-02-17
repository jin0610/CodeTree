### 완전 탐색 / 언덕깍기
import sys

N = int(input()) 
heights = [int(input()) for _ in range(N)]

# Write your code here!
min_price = sys.maxsize
min_height, max_height = min(heights), max(heights)

diff_range = max_height - min_height - 17
for i in range(diff_range + 1):
    plus, minus = i, diff_range - i
    price = 0

    new_min_height, new_max_height = min_height + i, max_height - minus

    for h in heights:
        if h < new_min_height:
            price += (new_min_height - h) ** 2
        if h > new_max_height:
            price += (h-new_max_height) ** 2

    min_price = min(min_price, price)

print(min_price)