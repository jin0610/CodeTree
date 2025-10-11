from collections import deque

class Deque:
    def __init__(self):
        self.dq = deque()

    # 정수 A를 deque 앞에 넣음
    def push_front(self, A):
        self.dq.appendleft(A)

    # 정수 A를 deque 뒤에 넣음
    def push_back(self, A):
        self.dq.append(A)

    # deque 앞에 있는 수 빼고, 출력
    def pop_front(self):
        print(self.dq.popleft())

    # deque 뒤에 있는 수 빼고, 출력
    def pop_back(self):
        print(self.dq.pop())

    # deque에 들어있는 정수의 개수
    def size(self):
        print(len(self.dq))

    # deque 비어있으면 1, 아니면 0
    def empty(self):
        if self.dq:
            print(0)
        else:
            print(1)

    # deque 가장 앞에 있는 정수 출력
    def front(self):
        print(self.dq[0])

    # deque 가장 뒤에 있는 정수 출력
    def back(self):
        print(self.dq[-1])

N = int(input())
dq = Deque()
for _ in range(N):
    com = input().split(' ')
    if com[0] == 'push_front':
        dq.push_front(com[1])
    elif com[0] == 'push_back':
        dq.push_back(com[1])
    elif com[0] == 'pop_front':
        dq.pop_front()
    elif com[0] == 'pop_back':
        dq.pop_back()
    elif com[0] == 'size':
        dq.size()
    elif com[0] == 'empty':
        dq.empty()
    elif com[0] == 'front':
        dq.front()
    else:
        dq.back()
