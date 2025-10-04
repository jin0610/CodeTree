strs = input()

# Please write your code here.
s = list()

def isCom(strs):
    s = list()

    for i in range(len(strs)):
        if strs[i] == "(":
            s.append("(")
        else:
            if s and s[-1] == "(":
                s.pop()
            else:
                break

    if s:
        return False
    return True

if isCom(strs):
    print('Yes')
else:
    print("No")