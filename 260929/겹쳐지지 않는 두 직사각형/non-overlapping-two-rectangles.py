import sys

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
max_sum_of_rect = -sys.maxsize

def not_is_overlap(rect1, rect2):
    rect1_r1, rect1_c1, rect1_r2, rect1_c2, _ = rect1
    rect2_r1, rect2_c1, rect2_r2, rect2_c2, _ = rect2

    if rect1_r2 < rect2_r1 or rect1_r1 > rect2_r2 or rect1_c1 > rect2_c2 or rect1_c2 < rect2_c1:
        return True
    return False

def get_sum_of_rectangle(r1, c1, r2, c2):
    sum_of_rectangle = 0
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            sum_of_rectangle += grid[r][c]

    return sum_of_rectangle

rectangles = []
for r1 in range(n):
    for c1 in range(m):
        for r2 in range(r1, n):
            for c2 in range(c1, m):
                sum_of_rect = get_sum_of_rectangle(r1, c1, r2, c2)
                rectangles.append((r1, c1, r2, c2, sum_of_rect))

count_of_rectangles = len(rectangles)
for i in range(count_of_rectangles):
    for j in range(i + 1, count_of_rectangles):
        rect1, rect2 = rectangles[i], rectangles[j]
        if not_is_overlap(rect1, rect2):
            max_sum_of_rect = max(max_sum_of_rect, rect1[4] + rect2[4])

print(max_sum_of_rect)