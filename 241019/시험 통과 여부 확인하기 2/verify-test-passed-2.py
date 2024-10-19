n = int(input())
cnt = 0
for i in range(n):
    scores = list(map(int, input().split()))
    score = sum(scores) / 4

    if( score >= 60):
        print("pass")
        cnt = cnt + 1
    else:
        print("fail")
print(cnt)