def max_rectangle_area_from_red_tiles(filename: str = "input.txt") -> int:
    points = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            x_str, y_str = line.split(",")
            x, y = int(x_str), int(y_str)
            points.append((x, y))

    max_area = 0
    n = len(points)

    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            width = abs(x1 - x2) + 1
            height = abs(y1 - y2) + 1
            area = width * height
            if area > max_area:
                max_area = area

    return max_area


if __name__ == "__main__":
    print(max_rectangle_area_from_red_tiles("input.txt"))
