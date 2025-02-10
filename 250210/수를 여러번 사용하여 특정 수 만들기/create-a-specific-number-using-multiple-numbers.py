### 수를 여러번 사용하여 특정 수 만들기
A, B, C = map(int, input().split())

result = 0
for i in range(C // A + 1):
    hap = A * i
    div_b = (C - hap) // B
    hap += div_b * B

    result = max(result, hap)

print(result)