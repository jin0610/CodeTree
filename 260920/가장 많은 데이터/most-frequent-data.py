N = int(input())

word_dict = dict()
for n in range(N):
    word = input()

    if word in word_dict.keys():
        word_dict[word] += 1
    else:
        word_dict[word] = 1

print(max(word_dict.values()))

