import sys

def reverse_number(num):

    return int(str(num)[::-1])

def main():

    tokens = sys.stdin.read().split()
    if not tokens:
        return

    n = int(tokens[0])

    numbers = [int(token) for token in tokens[1:1+n]]

    reversed_numbers = [reverse_number(num) for num in numbers]

    reversed_numbers.sort()

    print(" ".join(map(str, reversed_numbers)))

if __name__ == "__main__":
    main()
