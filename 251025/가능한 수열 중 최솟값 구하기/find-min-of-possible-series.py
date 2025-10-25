import sys
n = int(input())

def is_possible(numbers):
    for length in range(1, n // 2 + 1):
        for i in range(n - 2 * length + 1):
            if numbers[i : i + length] == numbers[i + length : i + 2*length]:
                return False

    return True

numbers = []
def backtracking(depth, cnt):
    global numbers

    if depth == cnt:
        if is_possible(numbers):
            print("".join(map(str,numbers)))
            sys.exit()
        return

    for i in range(4, 7):
        numbers.append(i)
        backtracking(depth, cnt + 1)
        numbers.pop()
    return

backtracking(n, 0)
