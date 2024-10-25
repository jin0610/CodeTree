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
    info.append(Region(name, address, region))
    if name > info[idx].name:
        idx = i

print(f"name {info[idx].name}\naddr {info[idx].address}\ncity {info[idx].region}")