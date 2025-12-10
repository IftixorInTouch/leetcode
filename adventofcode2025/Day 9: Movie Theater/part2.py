from collections import deque

def read_points(filename="input.txt"):
    points = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            x_str, y_str = line.split(",")
            x, y = int(x_str), int(y_str)
            points.append((x, y))
    return points


def compress_coords(values):
    vals = sorted(set(values))
    if not vals:
        return [], {}
    res = [vals[0]]
    for i in range(len(vals) - 1):
        a, b = vals[i], vals[i + 1]
        if b > a + 1:
            res.append(a + 1)
        res.append(b)
    index = {v: i for i, v in enumerate(res)}
    return res, index


def build_compressed_world(points):
    xs = [x for x, _ in points]
    ys = [y for _, y in points]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    xs_raw = xs + [min_x - 1, max_x + 1]
    ys_raw = ys + [min_y - 1, max_y + 1]

    xs_comp, x_index = compress_coords(xs_raw)
    ys_comp, y_index = compress_coords(ys_raw)
    W, H = len(xs_comp), len(ys_comp)

    wall = [[False] * W for _ in range(H)]

    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]

        ix1, iy1 = x_index[x1], y_index[y1]
        ix2, iy2 = x_index[x2], y_index[y2]

        if ix1 == ix2:
            step = 1 if iy2 > iy1 else -1
            for iy in range(iy1, iy2 + step, step):
                wall[iy][ix1] = True
        elif iy1 == iy2:
            step = 1 if ix2 > ix1 else -1
            for ix in range(ix1, ix2 + step, step):
                wall[iy1][ix] = True
        else:
            raise ValueError("Adjacent red tiles must be axis-aligned (same x or same y).")

    outside = [[False] * W for _ in range(H)]
    q = deque()

    sx = x_index[min_x - 1]
    sy = y_index[min_y - 1]
    outside[sy][sx] = True
    q.append((sx, sy))

    while q:
        x, y = q.popleft()
        if x + 1 < W and not outside[y][x + 1] and not wall[y][x + 1]:
            outside[y][x + 1] = True
            q.append((x + 1, y))
        if x - 1 >= 0 and not outside[y][x - 1] and not wall[y][x - 1]:
            outside[y][x - 1] = True
            q.append((x - 1, y))
        if y + 1 < H and not outside[y + 1][x] and not wall[y + 1][x]:
            outside[y + 1][x] = True
            q.append((x, y + 1))
        if y - 1 >= 0 and not outside[y - 1][x] and not wall[y - 1][x]:
            outside[y - 1][x] = True
            q.append((x, y - 1))

    bad = [[1 if outside[y][x] else 0 for x in range(W)] for y in range(H)]

    pref = [[0] * (W + 1) for _ in range(H + 1)]
    for y in range(H):
        row_sum = 0
        for x in range(W):
            row_sum += bad[y][x]
            pref[y + 1][x + 1] = pref[y][x + 1] + row_sum

    red_idx = [(x_index[x], y_index[y]) for (x, y) in points]

    return pref, red_idx, xs_comp, ys_comp


def rect_bad_sum(pref, x1, y1, x2, y2):
    left, right = min(x1, x2), max(x1, x2)
    top, bottom = min(y1, y2), max(y1, y2)
    return (
        pref[bottom + 1][right + 1]
        - pref[top][right + 1]
        - pref[bottom + 1][left]
        + pref[top][left]
    )


def max_rectangle_area_red_green_compressed(filename="input.txt"):
    points = read_points(filename)
    pref_bad, red_idx, xs_comp, ys_comp = build_compressed_world(points)

    max_area = 0
    n = len(points)

    for i in range(n):
        x1, y1 = points[i]
        ix1, iy1 = red_idx[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            ix2, iy2 = red_idx[j]

            if rect_bad_sum(pref_bad, ix1, iy1, ix2, iy2) == 0:
                width = abs(x1 - x2) + 1
                height = abs(y1 - y2) + 1
                area = width * height
                if area > max_area:
                    max_area = area

    return max_area


if __name__ == "__main__":
    print(max_rectangle_area_red_green_compressed("input.txt"))
