### 케이스 별로 나누기 - 좋은전략 추려내기 / 개발자의 가위바위보
N = int(input())
A, B = [], []
for i in range(N):
    a, b = input().split()
    # 비긴 경우 제외
    if a == b:
        continue
    A.append(int(a))
    B.append(int(b))

# Case1. 1-가위, 2-바위, 3-보 / 1-바위, 2-보, 3-가위 / 1-보, 2-가위, 3-바위
win = 0
for i in range(len(A)):
    if A[i] == 1 and B[i] == 3: win += 1
    elif A[i] == 2 and B[i] == 1: win+=1
    elif A[i] == 3 and B[i] == 2: win+=1

# Case2. 1-가위, 2-보, 3-바위 / 1-바위, 2-가위, 3-보  / 1-보, 2-바위, 3-가위
win2 = 0
for i in range(len(A)):
    if A[i] == 1 and B[i] == 2: win2 += 1
    elif A[i] == 2 and B[i] == 3: win2 +=1
    elif A[i] == 3 and B[i] == 1: win2 +=1

print(max(win, win2))
