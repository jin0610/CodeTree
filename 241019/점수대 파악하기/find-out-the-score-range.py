scores = list(map(int, input().split()))

result = [0] * 10

for score in scores:
    if(score == 0):
        break
    else:
        result[(score//10) -1] += 1

for i in range(len(result)-1, -1, -1):
    print(f"{str((i + 1) * 10)} - {result[i]}")