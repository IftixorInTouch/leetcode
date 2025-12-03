def max_k_subsequence(bank: str, k: int = 12) -> int:
    bank = bank.strip()
    n = len(bank)
    remove = n - k
    stack = []

    for ch in bank:
        while stack and remove > 0 and stack[-1] < ch:
            stack.pop()
            remove -= 1
        stack.append(ch)

    return int("".join(stack[:k]))


def main():
    total = 0
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            total += max_k_subsequence(line, 12)

    print(total)


if __name__ == "__main__":
    main()
