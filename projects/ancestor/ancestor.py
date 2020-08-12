
def earliest_ancestor(ancestors, starting_node):
    vertices = {}

    for parent, child in ancestors:
        if child not in vertices:
            vertices[child] = set()
        vertices[child].add(parent)

    if starting_node in vertices:
        parents = vertices[starting_node]

        while parents:
            children = parents
            parents = set()

            for child in children:
                if child in vertices:
                    parents = parents.union(vertices[child])

        if len(children) == 1:
            return children.pop()
        else:
            return min(children)
    else:
        return -1


if __name__ == "__main__":
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    print(earliest_ancestor(test_ancestors, 3))