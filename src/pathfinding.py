def dijkstra(start, end, nodes, edges):
    distances = {node['id']: float('inf') for node in nodes}
    previous = {node['id']: None for node in nodes}
    unvisited = {node['id'] for node in nodes}

    distances[start] = 0

    while unvisited:
        current = min(unvisited, key=lambda node_id: distances[node_id])
        if distances[current] == float('inf'):
            break
        if current == end:
            break
        unvisited.remove(current)

        neighbors = [edge for edge in edges if edge['source'] == current and edge['target'] in unvisited]
        for edge in neighbors:
            alt = distances[current] + edge['weight']
            if alt < distances[edge['target']]:
                distances[edge['target']] = alt
                previous[edge['target']] = current

    path = []
    current = end
    while current:
        path.insert(0, current)
        current = previous[current]
    return path