class Place:
    def __init__(self, idx, num,next_idx=0):
        self.idx = idx
        self.num = num
        self.next_idx = next_idx

N = int(input())
arr = list(map(int, input().split()))

arr2 = []
for i in range(N):
    arr2.append(Place(i, arr[i]))

arr2.sort(lambda x : x.num)

for i in range(N):
    arr2[i].next_idx = i + 1

arr2.sort(lambda x:x.idx)
for i in range(N):
    print(arr2[i].next_idx, end=" ")