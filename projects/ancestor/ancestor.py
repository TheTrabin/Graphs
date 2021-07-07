import copy
from util import Stack, Queue


def add_vertex(vertices, vertex_id):

    if vertices.get(vertex_id) is None:
        vertices[vertex_id] = set()


def add_edge(vertices, v1, v2):

    if v1 not in vertices or v2 not in vertices:
        print("Attempting to add edge to non-existing nodes")
        return
    vertices[v1].add(v2)


def get_neighbors(vertices, vertex_id):

    return vertices[vertex_id]


def earliest_ancestor(ancestors, starting_node):

    vertices = {}
    s = Stack()

    for pair in ancestors:
        add_vertex(vertices, pair[0])
        add_vertex(vertices, pair[1])
        add_edge(vertices, pair[1], pair[0])

    path = [starting_node]
    s.push(path)

    visited = set()

    longest_path = []

    while s.size() > 0:
        p = s.pop()

        last = p[-1]

        if len(longest_path) == len(p) and last < longest_path[-1]:
            longest_path = p

        if len(longest_path) < len(p):
            longest_path = p

        if last not in visited:
            visited.add(last)

            for neighbor in get_neighbors(vertices, last):
                path = copy.copy(p)
                path.append(neighbor)
                s.push(path)

    if len(longest_path) == 1:
        return -1

    else:
        return longest_path[-1]
