### 자리마다 숫자를 정하는 완전탐색 / 두 가지로 열리는 자물쇠
N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

# Write your code here!
# 겹치는 경우
cnt_a, cnt_b, cnt_c = 0, 0, 0
for n in range(N+2):
    if abs(a1-n) <= 2 and abs(a2 - n) <= 2:
        cnt_a += 1
    if abs(b1-n) <= 2 and abs(b2 - n) <= 2:
        cnt_b += 1
    if abs(c1-n) <= 2 and abs(c2 - n) <= 2:
        cnt_c += 1

cnt = cnt_a * cnt_b * cnt_c
print(250-cnt)

        
    
    

