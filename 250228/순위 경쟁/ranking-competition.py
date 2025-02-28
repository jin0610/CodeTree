n = int(input())

honor = "012" # A :0, B : 1, C:2
score = [0, 0, 0] # [a, b, c]
cnt = 0
for _ in range(n):
    ci, si = input().split()
    si = int(si)
    if ci == 'A':
        score[0] += si
    elif ci == 'B':
        score[1] += si
    else:
        score[2] += si

    max_idx = [i for i in range(3) if score[i] == max(score)]
    new_honor = ''.join(map(str, max_idx))

    if honor != new_honor:
        cnt += 1
        honor = new_honor
print(cnt)