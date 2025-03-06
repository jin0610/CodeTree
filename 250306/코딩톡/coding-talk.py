### 케이스별로 나누기 (일어난 상황에 대한 추론) / 코딩
n, m, p = map(int, input().split())
messages = [tuple(input().split()) for _ in range(m)]
c = [msg[0] for msg in messages]
u = [int(msg[1]) for msg in messages]

# 채팅방에 들어와 있는 사람들
person = []
for i in range(n):
    person.append(chr(ord('A') + i))

# 메시지를 쓴 시점 이후 메시지를 쓴 사람들 제외(메시지를 쓴 사람도 제외)
for i in range(p-1, n):
    if c[i] in person:
        person.remove(c[i])

print(' '.join(person))