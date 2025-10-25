import sys
n = int(input())

def is_possible(numbers):
    for length in range(2, n // 2 + 1):
        for i in range(n - 2 * length + 1):
            list_1 = numbers[i : i + length]
            list_2 = numbers[i + length : i + 2 * length]
            if list_1 == list_2:
                return False

    return True

numbers = []
def backtracking(depth, cnt):
    global numbers

    if depth == cnt:
        if is_possible(numbers):
            print("".join(map(str,numbers)))
            sys.exit(0)
        return

    for i in range(4, 7):
        if numbers and numbers[-1] == i:
            continue
        numbers.append(i)
        backtracking(depth, cnt + 1)
        numbers.pop()
    return

backtracking(n, 0)
