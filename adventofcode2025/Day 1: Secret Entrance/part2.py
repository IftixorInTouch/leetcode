def count_all_zero_hits(filename: str) -> int:
    position = 50
    zeros = 0

    with open(filename) as f:
        moves = [line.strip() for line in f if line.strip()]

    for move in moves:
        direction = move[0]
        steps = int(move[1:])
        step = 1 if direction == "R" else -1

        for _ in range(steps):
            position = (position + step) % 100
            if position == 0:
                zeros += 1

    return zeros


if __name__ == "__main__":
    answer = count_all_zero_hits("input.txt")
    print(answer)
