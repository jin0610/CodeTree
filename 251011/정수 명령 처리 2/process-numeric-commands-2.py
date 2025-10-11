from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()

    # 정수 A를 큐에 넣
    def push(self, A):
        self.dq.append(A)

    def pop(self):
        print(self.dq.popleft())
        

    def size(self):
        print(len(self.dq))
    
    def empty(self):
        if self.dq:
            return print(0)
        else:
            return print(1)
    
    def front(self):
        print(self.dq[0])


N = int(input())

deq = Queue()

for i in range(N):
    com = input().split(' ')

    if com[0] == 'push':
        deq.push(com[1])
    elif com[0] == 'pop':
        deq.pop()
    elif com[0] == 'size':
        deq.size()
    elif com[0] == 'empty':
        deq.empty()
    else:
        deq.front()

