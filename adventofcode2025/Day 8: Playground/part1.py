from itertools import combinations
from collections import Counter


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n

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
        self.size[ra] += self.size[rb]
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


def solve(filename="input.txt", num_pairs=1000):
    points = read_points(filename)
    n = len(points)

    pairs = []
    for i, j in combinations(range(n), 2):
        d2 = squared_dist(points[i], points[j])
        pairs.append((d2, i, j))

    pairs.sort(key=lambda x: x[0])

    dsu = DSU(n)

    limit = min(num_pairs, len(pairs))
    for k in range(limit):
        _, i, j = pairs[k]
        dsu.union(i, j)

    comp_sizes = Counter()
    for i in range(n):
        root = dsu.find(i)
        comp_sizes[root] = dsu.size[root]

    largest = sorted(comp_sizes.values(), reverse=True)[:3]
    while len(largest) < 3:
        largest.append(1)

    ans = largest[0] * largest[1] * largest[2]
    print(ans)


if __name__ == "__main__":
    solve("input.txt", num_pairs=1000)
