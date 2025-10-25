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
def backtracking(cnt):
    global numbers

    if cnt == n:
        if is_possible(numbers):
            print("".join(map(str,numbers)))
            sys.exit(0)
        return

    for i in range(4, 7):
        if numbers and numbers[-1] == i:
            continue
        numbers.append(i)
        backtracking(cnt + 1)
        numbers.pop()
    return

backtracking(0)
