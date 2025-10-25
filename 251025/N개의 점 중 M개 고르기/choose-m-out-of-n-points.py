import sys

n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

def Euclidean(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
    return dist

# 두 점 사이의 거리가 가장 먼 두점의 거리 구하기
def get_min_dist_diff():
    global selected_points
    max_dist = 0

    for i in range(m-1):
        for j in range(i + 1, m):
            max_dist = max(max_dist, Euclidean(selected_points[i], selected_points[j]))
    
    return max_dist

# M개의 포인트 구하기
selected_points = []
answer = sys.maxsize
def choose_point(curr_idx, cnt):
    global points, selected_points, answer

    if cnt == m:
        answer = min(answer, get_min_dist_diff())
        return

    for i in range(curr_idx, n):
        selected_points.append(points[i])
        choose_point(i + 1, cnt + 1)
        selected_points.pop()

    return

choose_point(0, 0)
print(answer)