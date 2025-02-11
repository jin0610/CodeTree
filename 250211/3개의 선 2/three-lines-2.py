### 완전탐색 / 3개의 선 2
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Write your code here!
answer = 0

for i in range(11):
    for j in range(11):
        for k in range(11):
    
            # x 축에 평행한 선 3개
            success=True
            for x, y in points:
                if x == i or x == j or x == k:
                    continue
                success = False
            if success:
                answer = 1

            # x 축에 평행한 선 2개, y축에 평행한 선 1개
            success=True
            for x, y in points:
                if x == i or x == j or y == k:
                    continue
                success = False
            if success:
                answer = 1

            # x 축에 평행한 선 1개, y축에 평행한 선 2개
            success=True
            for x, y in points:
                if x == i or y == j or y == k:
                    continue
                success = False
            if success:
                answer = 1

            # y 축에 평행한 선 3개
            success=True
            for x, y in points:
                if y == i or y == j or y == k:
                    continue        
                success = False
            if success:
                answer = 1

print(answer)