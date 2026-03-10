from sortedcontainers import SortedSet

T = int(input())

s = SortedSet()
for _ in range(T):
    K = int(input())
    for _ in range(K):
        w, n = input().split()

        if w == "I":
            s.add(int(n))
        else:
            if len(s) != 0:
                if n == "1":
                    s.remove(s[-1])
                else:
                    s.remove(s[0])

    if len(s) == 0:
        print("EMPTY")
    else:
        print(s[-1], s[0])