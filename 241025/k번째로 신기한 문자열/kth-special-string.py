n, k, T = input().split()
n, k,T = int(n), int(k), list(T)

ss = []
for _ in range(n):
    w = list(input())
    if w[:len(T)] == T:
        ss.append(w)

ss.sort()
print(''.join(ss[k-1]))