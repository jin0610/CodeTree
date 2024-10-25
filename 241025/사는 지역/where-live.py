class Region:
    def __init__(self, name, address, region):
        self.name = name
        self.address =address
        self.region = region

n = int(input())

idx = 0
info = []
for i in range(n):
    name, address, region = input().split()

    if name > info[idx].info:
        idx = i

print(f"name {info[idx].name}\naddr {info[idx].address}\ncity {info[idx].region}")