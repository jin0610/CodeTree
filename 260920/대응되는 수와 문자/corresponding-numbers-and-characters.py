N, M = map(int, input().split())

word_dict = dict()
reverse_dict = dict()
for n in range(N):
    w = input()
    word_dict[w] = n + 1
    reverse_dict[n+1] = w

for m in range(M):
    w = input()
    try:
        w = int(w)
        print(reverse_dict[w])
    except:
        print(word_dict[w])
    