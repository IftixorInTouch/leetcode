import math

def read_input(filename="input.txt"):
    with open(filename, "r") as f:
        lines = [line.rstrip("\n") for line in f]
    return [line for line in lines if line.strip() != ""]


def parse_problems(lines):
    height = len(lines)
    width = max(len(line) for line in lines)

    lines = [line.ljust(width) for line in lines]

    sep = []
    for c in range(width):
        if all(lines[r][c] == " " for r in range(height)):
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

    return problems, lines


def solve():
    lines = read_input("input.txt")

    problems, lines = parse_problems(lines)
    height = len(lines)

    grand_total = 0

    for start, end in problems:
        numbers = []

        for r in range(height - 1):
            chunk = lines[r][start:end + 1].strip()
            if chunk:
                numbers.append(int(chunk))

        op_segment = lines[height - 1][start:end + 1]
        op = next(ch for ch in op_segment if ch in "+*")

        if op == "+":
            result = sum(numbers)
        else:
            result = math.prod(numbers)

        grand_total += result

    print(grand_total)


if __name__ == "__main__":
    solve()
