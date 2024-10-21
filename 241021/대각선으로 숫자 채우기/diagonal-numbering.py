N,M = list(map(int, input().split()))

result = [[0 for _ in range(M)] for _ in range(N)]

num = 1
# row col

for m in range(M+N-1):
    for n in range(m+1):
        try:
            # print(n, m-n, num)

            result[n][m-n]= num
            num = num + 1
        except:
            pass

"""
0,0     0,6
        1,5
0,1     2,4
1,0     3,3

0,2
1,1
2,0

0,3
1,2
2,1
3,0

0,4
1,3
2,2
3,1


"""
for n in range(N):
    print(*result[n])