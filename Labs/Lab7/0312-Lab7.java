package Labs.Lab7;

public int findTheCity(int n, int[][] edges, int distanceThreshold) {
    int[][] distance = new int[n][n];
    for (int i = 0; i < n; i++) {
        Arrays.fill(distance[i], Integer.MAX_VALUE);
        distance[i][i] = 0;
    }//for

    // Fill in distance matrix based on given edges
    for (int[] edge : edges) {
        int from = edge[0];
        int to = edge[1];
        int weight = edge[2];
        distance[from][to] = weight;
        distance[to][from] = weight;
    }//for

    // Floyd-Warshall algorithm to find shortest distances
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (distance[i][k] != Integer.MAX_VALUE && distance[k][j] != Integer.MAX_VALUE) {
                    distance[i][j] = Math.min(distance[i][j], distance[i][k] + distance[k][j]);
                }//if
            }//for
        }//for
    }//for

    int minReachableCities = Integer.MAX_VALUE;
    int resultCity = -1;
    // Iterate over each city
    for (int i = 0; i < n; i++) {
        int reachableCities = 0;
        for (int dist : distance[i]) {
            if (dist <= distanceThreshold) reachableCities++;               
        }//for
        if (reachableCities <= minReachableCities) {
            minReachableCities = reachableCities;
            resultCity = i;
        } //if
    }//for
    return resultCity;
}//findthecity
