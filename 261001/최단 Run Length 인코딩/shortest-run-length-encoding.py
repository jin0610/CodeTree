from collections import defaultdict
import sys

a = input()

def runLengthEncoding(string):
    run_length_encoding = string[0]

    cnt = 1
    for s in string[1:]:
        if run_length_encoding[-1] != s:
            run_length_encoding += f"{cnt}{s}"
            cnt = 1
        else:
            cnt += 1
    run_length_encoding += f"{cnt}"

    return len(run_length_encoding)

def shift(string):
    min_length = sys.maxsize

    curr_string = string
    while True:

        new_string = curr_string[-1] + curr_string[:-1]
        min_length = min(min_length, runLengthEncoding(new_string))

        if new_string == string:
            break

        curr_string = new_string

    return min_length

print(shift(a))
    
