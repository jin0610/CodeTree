strs = input()

# Please write your code here.
def isCom(strs):
    s = list()

    for i in range(len(strs)):
        if strs[i] == "(":
            s.append("(")
        else:
            if s and s[-1] == "(":
                s.pop()
            else:
                return False

    if s:
        return False
    else:
        return True

if isCom(strs):
    print('Yes')
else:
    print("No")