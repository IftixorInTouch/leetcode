def count_accessible_rolls(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]

    total = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@':
                continue

            neighbor_at_count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == '@':
                        neighbor_at_count += 1

            if neighbor_at_count < 4:
                total += 1

    return total


def main():
    with open("input.txt") as f:
        grid = [line.rstrip("\n") for line in f if line.strip()]

    result = count_accessible_rolls(grid)
    print(result)


if __name__ == "__main__":
    main()
