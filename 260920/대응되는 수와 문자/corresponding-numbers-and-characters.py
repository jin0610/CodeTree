N, M = map(int, input().split())

word = [""] + [input() for _ in range(N)]

word_dict = dict()
for i, w in enumerate(word):
    word_dict[w] = i

for m in range(M):
    w = input()
    if w.isdigit():
        print(word[int(w)])

    else:
        print(word_dict[w])
    