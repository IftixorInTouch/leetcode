import math


def read_input(filename="input.txt"):
    with open(filename, "r") as f:
        lines = [line.rstrip("\n") for line in f]
    return [line for line in lines if line.strip() != ""]


def find_problems(lines):
    """Return (problems, padded_lines)
    problems = list of (start_col, end_col) for each vertical problem block.
    """
    height = len(lines)
    width = max(len(line) for line in lines)

    padded = [line.ljust(width) for line in lines]

    sep = []
    for c in range(width):
        if all(padded[r][c] == " " for r in range(height)):
            sep.append(True)
        else:
            sep.append(False)

    problems = []
    c = 0
    while c < width:
        if sep[c]:
            c += 1
            continue
        start = c
        while c < width and not sep[c]:
            c += 1
        end = c - 1
        problems.append((start, end))

    return problems, padded


def solve_cephalopod_math(filename="input.txt"):
    lines = read_input(filename)
    problems, lines = find_problems(lines)

    height = len(lines)
    grand_total = 0

    for start, end in problems:
        numbers = []

        for col in range(start, end + 1):
            digits = [lines[row][col] for row in range(height - 1)]
            s = "".join(ch for ch in digits if ch != " ")
            if s:
                numbers.append(int(s))

        op_row = lines[height - 1][start:end + 1]
        op = next(ch for ch in op_row if ch in "+*")

        if op == "+":
            result = sum(numbers)
        else:
            result = math.prod(numbers)

        grand_total += result

    print(grand_total)


if __name__ == "__main__":
    solve_cephalopod_math("input.txt")
