
def adjacency_matrix(vertices, edges):
    n = len(vertices)
    matrix = [[0] * n for _ in range(n)]
    for u, v in edges:
        matrix[u - 1][v - 1] = 1
        matrix[v - 1][u - 1] = 1
    return matrix

def incidence_matrix(vertices, edges):
    n = len(vertices)
    m = len(edges)
    matrix = [[0] * m for _ in range(n)]
    for j, (u, v) in enumerate(edges):
        matrix[u - 1][j] = 1
        matrix[v - 1][j] = 1
    return matrix

def dfs(v, graph, visited, component):
    visited.add(v)
    component.append(v)
    for neighbor in graph[v]:
        if neighbor not in visited:
            dfs(neighbor, graph, visited, component)

def connected_components(vertices, edges):
    graph = {v: [] for v in vertices}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited = set()
    components = []
    for v in vertices:
        if v not in visited:
            component = []
            dfs(v, graph, visited, component)
            components.append(component)
    return components
