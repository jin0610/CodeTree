s = input()

ss=[]
cnt = 1

while s != '0':
    if cnt % 2 == 1:
        ss.append(s)

    s = input()
    cnt +=1
    

print(cnt-1)
for i in ss:
    print(i)