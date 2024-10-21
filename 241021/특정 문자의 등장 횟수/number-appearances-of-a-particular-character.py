strs = input()

ee = 0
eb = 0

for i in range(len(strs)-1):
    if(strs[i] == "e" and strs[i+1] == "e"):
        ee += 1
    
    if(strs[i] == "e" and strs[i+1] == "b"):
        eb +=1

print(ee, eb)