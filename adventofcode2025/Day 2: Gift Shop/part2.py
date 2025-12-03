def add_invalid_ids(filename: str) -> int:
    with open(filename) as f:
        ranges = f.read().split(",")
    total = 0
    for part in ranges:
        start, end = map(int, part.split("-"))
        for x in range(start, end + 1):
            if is_invalid_id(x):
                total += x
    return total


def is_invalid_id(n: int) -> bool:
    s = str(n)
    if len(s) < 2:
        return False
    return s in (s + s)[1:-1]


if __name__ == "__main__":
    answer = add_invalid_ids("input.txt")
    print(answer)
