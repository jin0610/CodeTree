N = int(input())

length = 0
cnt = 0

for n in range(N):
    s = input()
    length = length + len(s)
    if(s[0] == 'a'):
        cnt += 1

print(length, cnt)