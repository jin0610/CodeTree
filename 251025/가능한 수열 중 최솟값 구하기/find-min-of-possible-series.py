import sys
n = int(input())

def is_possible(numbers):
    length = len(numbers)
    for l in range(2, length // 2 + 1):
        for i in range(length - 2 * l + 1):
            list_1 = numbers[i : i + l]
            list_2 = numbers[i + l : i + 2 * l]
            if list_1 == list_2:
                return False
    return True

numbers = []
def backtracking(cnt):
    global numbers

    if cnt == n:
        print("".join(map(str,numbers)))
        sys.exit(0)
        return

    for i in range(4, 7):
        if numbers and numbers[-1] == i:
            continue
        numbers.append(i)
        if is_possible(numbers):
            backtracking(cnt + 1)
        numbers.pop()
    return

backtracking(0)
