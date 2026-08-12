import heapq
import itertools
from collections import Counter

class DisjointSet:
    def find(self, x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]

        return x

    def union(self, u: int, v: int) -> bool:
        ru, rv = self.find(u), self.find(v)
        if ru == rv:
            return False

        parent[ru] = rv
        return True

def prob08_1() -> int:
    points = []
    with open('./input/prob08.txt') as f:
        lines = f.readlines()
        for line in lines:
            coords = line.strip().split(',')
            coords = tuple(int(x) for x in coords)
            points.append(coords)

    n = len(points)
    global parent
    parent = list(range(n))

    edges = [(sum((a - b) ** 2 for a, b in zip(points[i], points[j])), i, j) for i, j in itertools.combinations(range(n), 2)]
    edges.sort()
    dset = DisjointSet()
    for d2, i, j in edges[:1000]:
        dset.union(i, j)

    sizes = Counter(dset.find(i) for i in range(n))
    total = 1
    for root, count in sizes.most_common(3):
        total *= count

    return total

def prob08_2() -> int:
    points = []
    with open('./input/prob08.txt') as f:
        lines = f.readlines()
        for line in lines:
            coords = line.strip().split(',')
            coords = tuple(int(x) for x in coords)
            points.append(coords)

    n = len(points)
    global parent
    parent = list(range(n))

    # kruskal's:
    edges = [(sum((a - b) ** 2 for a, b in zip(points[i], points[j])), i, j) for i, j in itertools.combinations(range(n), 2)]
    edges.sort()
    dset = DisjointSet()
    components = n
    for d2, i, j in edges:
        if dset.union(i, j):
            components -= 1

        if components == 1:
            return points[i][0] * points[j][0]

    return -1
