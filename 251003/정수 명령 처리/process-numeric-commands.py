class Stack:
    def __init__(self):
        self.items = [] # 빈 스택 생성

    def push(self, item):
        self.items.append(item)

    def empty(self):        # 스택이 비어있으면 True
        if self.items:
            print(0)
        else:
            print(1)

    def size(self):         # 스택에 있는 데이터 수 출력
        print(len(self.items))

    def pop(self):          # 가장 위에 있는 수 제거
        num = self.items.pop()
        print(num)
    
    def top(self):          # 가장 위에있는 수 출력
        print(self.items[-1])

N = int(input())

s = Stack()

for i in range(N):
    com = input().split(' ')

    if com[0] == 'push':
        s.push(com[1])
    elif com[0] == 'pop':
        s.pop()
    elif com[0] == 'size':
        s.size()
    elif com[0] == 'empty':
        s.empty()
    else:
        s.top()
    



    