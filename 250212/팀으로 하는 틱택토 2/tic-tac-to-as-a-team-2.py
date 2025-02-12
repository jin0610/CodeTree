### 완전 탐색 / 팀으로 하는 틱택토 2
inp = [list(map(int, list(str(input())))) for _ in range(3)]

# Write your code here!
answer = 0
# 가로 
for i in range(3):
    if len(set(inp[i])) == 2:
        answer += 1

# 세로
for i in range(3):
    arr_1 = set()
    for j in range(3):
        arr_1.add(inp[j][i])
    if len(set(arr_1)) == 2:
        answer+=1

# 대각선
arr_1 = set()
arr_2 = set()
for i in range(3):
    arr_1.add(inp[i][i])
    arr_2.add(inp[i][2-i])

if len(arr_1) == 2:
    answer+=1
if len(arr_2) == 2:
    answer+=1

print(answer)
        

        




