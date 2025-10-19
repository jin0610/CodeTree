import sys
N, M = map(int,input().split())
blocks = [
    int(input())
    for _ in range(N)
]

if M == 1:
    print(0)
    sys.exit()
def isSequence():
    global blocks, M
    for i in range(len(blocks)-1):
        cnt = 1
        for j in range(i + 1, len(blocks)):
            if blocks[i] != blocks[j]:
                break
            cnt += 1
        if cnt >= M:
            return True
    return False

def remove_num():
    global blocks, M
    temp, idx, temp_idx = [], [], []
    for i in range(len(blocks)-1):
        cnt = 1
        temp_idx.append(i)
        for j in range(i + 1, len(blocks)):
            if blocks[i] != blocks[j]:
                break
            cnt += 1
            temp_idx.append(j)
        if cnt >= M:
            idx = idx + temp_idx
        temp_idx = []

    for i in range(len(blocks)):
        if i not in idx:
            temp.append(blocks[i])

    blocks = temp[:]

while True:
    if not isSequence():
        break
    remove_num()

print(len(blocks))
if len(blocks) > 0:
    for n in blocks:
        print(n)
    
