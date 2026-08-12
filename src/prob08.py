import heapq
import itertools
from collections import Counter

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
    
    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]

        return x

    def union(u: int, v: int):
        ru, rv = find(u), find(v)
        if ru == rv:
            return
        else:
            parent[ru] = parent[rv]

    edges = [(sum((a - b) ** 2 for a, b in zip(points[i], points[j])), i, j) for i, j in itertools.combinations(range(n), 2)]
    edges.sort()
    for d2, i, j in edges[:1000]:
        union(i, j)

    sizes = Counter(find(i) for i in range(n))
    total = 1
    for root, count in sizes.most_common(3):
        total *= count

    return total
