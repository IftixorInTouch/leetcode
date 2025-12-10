def count_splits(filename="input.txt"):
    with open(filename, "r") as f:
        grid = [line.rstrip("\n") for line in f]

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

    splits = 0
    beams = {start_col}

    for r in range(start_row + 1, rows):
        new_beams = set()
        for c in beams:
            cell = grid[r][c]
            if cell in (".", "S"):
                new_beams.add(c)
            elif cell == "^":
                splits += 1
                if c - 1 >= 0:
                    new_beams.add(c - 1)
                if c + 1 < cols:
                    new_beams.add(c + 1)
            else:
                raise ValueError(f"Unexpected cell '{cell}' at ({r},{c})")
        beams = new_beams

    return splits


if __name__ == "__main__":
    print(count_splits("input.txt"))
