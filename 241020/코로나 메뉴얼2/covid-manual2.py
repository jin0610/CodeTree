info = []

# A, B, C, D 인원 수
result = [0]*4
cnt = 0
for i in range(3):
    info = list(input().split())
    if (info[0] == "Y" and int(info[1]) >= 37):
        result[0] += 1
    elif (info[0] == "N" and int(info[1]) >= 37):
        result[1] += 1
    elif (info[0] == "Y" and int(info[1]) < 37):
        result[2] += 1
    else:
        result[3] += 1

if(result[0] >= 2):
    result.append("E")

for i in range(len(result)):
    print(result[i], end= " ")