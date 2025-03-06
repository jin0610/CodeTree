### 케이스별로 나누기 (일어난 상황에 대한 추론) / 코딩
import sys
n, m, p = map(int, input().split())
messages = [list(input().split()) for _ in range(m)]

# 채팅방에 들어와 있는 사람들
person = []
for i in range(n):
    person.append(chr(ord('A') + i))

# 만약 message를 안본 수가 0이라면 공백 출력
if messages[p-1][1] == '0':
    print()
    sys.exit(0)

# 메시지를 쓴 시점 이후 메시지를 쓴 사람들 제외(메시지를 쓴 사람도 제외)
for i in range(p-1, m):
    if messages[i][0] in person:
        person.remove(messages[i][0])

print(' '.join(person))