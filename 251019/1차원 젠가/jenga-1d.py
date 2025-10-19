n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

def delete(s, e):
    global blocks
    temp = []

    for i in range(len(blocks)):
        if s - 1 <= i < e:
            continue
        temp.append(blocks[i])
    blocks = temp[:]
    
delete(s1, e1)
delete(s2, e2)
print(len(blocks))
if len(blocks) != 0:
    for b in blocks:
        print(b)