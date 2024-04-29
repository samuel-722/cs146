def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    distance = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        distance[i][i] = 0
    for u, v, w in edges:
        distance[u][v] = w
        distance[v][u] = w
    
    # Floyd-Warshall algorithm to find shortest distances
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    
    # Initialize variables to store result
    min_reachable_cities = float('inf')
    result_city = -1
    
    # Go through and update result
    for i in range(n):
        reachable_cities = sum(dist <= distanceThreshold for dist in distance[i])
        if reachable_cities <= min_reachable_cities:
            min_reachable_cities = reachable_cities
            result_city = i
    
    return result_city