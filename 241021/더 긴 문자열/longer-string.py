s1, s2 = list(input().split())


if len(s1) > len(s2):
    print(s1, len(s1))
elif len(s1) < len(s2):
    print(s2, len(s2))
else:
    print('same')