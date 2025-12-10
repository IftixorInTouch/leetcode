def count_neighbors(grid, r, c):
    rows = len(grid)
    cols = len(grid[0])
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1),
    ]
    cnt = 0
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if grid[nr][nc] == '@':
                cnt += 1
    return cnt


def simulate_removal(grid):
    rows = len(grid)
    cols = len(grid[0])
    total_removed = 0

    while True:
        removable = []

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != '@':
                    continue
                if count_neighbors(grid, r, c) < 4:
                    removable.append((r, c))

        if not removable:
            break

        for r, c in removable:
            grid[r][c] = '.'

        total_removed += len(removable)

    return total_removed


def main():
    with open("input.txt") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]

    grid = [list(row) for row in lines]

    result = simulate_removal(grid)
    print(result)


if __name__ == "__main__":
    main()
