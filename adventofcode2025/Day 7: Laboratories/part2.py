def count_timelines(filename="input.txt"):
    with open(filename, "r") as f:
        grid = [line.rstrip("\n") for line in f]

    grid = [row for row in grid if row.strip() != ""]

    rows = len(grid)
    cols = len(grid[0])

    start_row = start_col = None
    for r, row in enumerate(grid):
        if "S" in row:
            start_row = r
            start_col = row.index("S")
            break

    if start_row is None:
        raise ValueError("No S found in input")

    counts = [0] * cols
    counts[start_col] = 1

    for r in range(start_row + 1, rows):
        new_counts = [0] * cols
        for c, n in enumerate(counts):
            if n == 0:
                continue
            cell = grid[r][c]
            if cell in (".", "S"):
                new_counts[c] += n
            elif cell == "^":
                if c - 1 >= 0:
                    new_counts[c - 1] += n
                if c + 1 < cols:
                    new_counts[c + 1] += n
            else:
                raise ValueError(f"Unexpected cell '{cell}' at ({r}, {c})")
        counts = new_counts

    return sum(counts)


if __name__ == "__main__":
    print(count_timelines("input.txt"))
