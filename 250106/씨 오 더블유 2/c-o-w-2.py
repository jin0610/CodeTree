### 자리수 단위로 완전탐색 / 씨 오 더블유2
n = int(input())
str = input()

# Write your code here!
result = 0
for c in range(n-2):
    if str[c] == "C":
        for o in range(c+1, n-1):
            if str[o] == "O":
                for w in range(o+1, n):
                    if str[w] == "W":
                        result += 1
print(result)
