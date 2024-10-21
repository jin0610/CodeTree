s1, s2 = list(input().split())
s1, s2 = list(s1), list(s2)
s2[:2] = s1[:2]

print(''.join(s2))