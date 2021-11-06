def dfs(visited, graph, node):
    result = []
    if node not in visited:
        visited.add(node)
        result.append(node)
        for child in graph[node]:
            temp = dfs(visited, graph, child)
            for value in temp:
                result.append(value)
    return result

def dfsHandler(graph, root, element=None):
    if graph == {}:
        return ([], False)
    result = dfs(set(), graph, root)
    return (result, element in result)