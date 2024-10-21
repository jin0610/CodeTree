s, q = list(input().split())

s, q = list(s), int(q)

quests = [list(input().split()) for _ in range(q)]

result = []

for quest in quests:
    i, a, b = quest
    i = int(i)
    s2 = s.copy()
    
    if(i == 1):
        a, b = int(a), int(b)
        s2[a-1], s2[b-1] = s2[b-1], s2[a-1]
        
    else:
        for i in range(len(s)):
            if(s[i] == a):
                s2[i] = b
    print("".join(s2))