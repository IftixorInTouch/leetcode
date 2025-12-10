from itertools import combinations


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True


def read_points(filename="input.txt"):
    points = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            x, y, z = map(int, line.split(","))
            points.append((x, y, z))
    return points


def squared_dist(p, q):
    return ((p[0] - q[0]) ** 2 +
            (p[1] - q[1]) ** 2 +
            (p[2] - q[2]) ** 2)


def solve(filename="input.txt"):
    points = read_points(filename)
    n = len(points)

    pairs = []
    for i, j in combinations(range(n), 2):
        d2 = squared_dist(points[i], points[j])
        pairs.append((d2, i, j))

    pairs.sort(key=lambda x: x[0])

    dsu = DSU(n)
    components = n
    last_pair = None

    for d2, i, j in pairs:
        if dsu.union(i, j):
            components -= 1
            if components == 1:
                last_pair = (i, j)
                break

    if last_pair is None:
        raise RuntimeError("Graph was already connected or something went wrong")

    i, j = last_pair
    x1 = points[i][0]
    x2 = points[j][0]
    result = x1 * x2
    print(result)


if __name__ == "__main__":
    solve("input.txt")
