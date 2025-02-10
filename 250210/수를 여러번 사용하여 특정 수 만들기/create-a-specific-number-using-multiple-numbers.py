### 수를 여러번 사용하여 특정 수 만들기
A, B, C = map(int, input().split())

div_a = C // A
div_b = C // B

max_result= 0
for a in range(div_a + 1):
    for b in range(div_b + 1):
        hap = A * a + B * b
        if hap <= C:
            max_result = max(max_result, hap)
        else:
            continue

print(max_result)
