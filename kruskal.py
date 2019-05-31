parent = dict()
rank = dict()


def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0


def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]


def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
        if rank[root1] == rank[root2]: rank[root2] += 1


def kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)
        minimum_spanning_tree = set()
        edges = list(graph['edges'])
        edges.sort()
    # print edges
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)

    return sorted(minimum_spanning_tree)


#  (peso 'vertice1', 'vertice2'),

graph = {
    'vertices': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i'],
    'edges': set([
        (240, 'a', 'b'),
        (210, 'a', 'c'),
        (340, 'a', 'd'),
        (280, 'a', 'e'),
        (200, 'a', 'f'),
        (345, 'a', 'g'),
        (120, 'a', 'h'),
        (265, 'b', 'c'),
        (175, 'b', 'd'),
        (215, 'b', 'e'),
        (180, 'b', 'f'),
        (185, 'b', 'g'),
        (155, 'b', 'h'),
        (260, 'c', 'd'),
        (115, 'c', 'e'),
        (350, 'c', 'f'),
        (435, 'c', 'g'),
        (195, 'c', 'h'),
        (160, 'd', 'e'),
        (330, 'd', 'f'),
        (295, 'd', 'g'),
        (230, 'd', 'h'),
        (360, 'e', 'f'),
        (400, 'e', 'g'),
        (170, 'e', 'h'),
        (175, 'e', 'g'),
        (205, 'e', 'h'),
        (305, 'f', 'h'),

    ])
}



print('(peso, ''coordenadas)')

print(kruskal(graph))