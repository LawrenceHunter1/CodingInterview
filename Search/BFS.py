def bfs(visited, graph, node):
    visited.add(node)
    queue = [node]
    result = [node]

    while queue:
        for child in graph[queue.pop(0)]:
            if child not in visited:
                visited.add(child)
                result.append(child)
                queue.append(child)
    return result

def bfsHandler(graph, root, element=None):
    if graph == {}:
        return ([], False)
    result = bfs(set(), graph, root)
    return (result, element in result)