#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]

    answer = 0
    for num in arguments:
        answer += int(num)
    print(answer)
