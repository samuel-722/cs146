def canFinish(numCourses, prerequisites):
    graph = {i: [] for i in range(numCourses)}
    for course, prereq in prerequisites:
        graph[course].append(prereq)
    
    visited = [0] * numCourses

    def dfs(course, visited):
        visited[course] = 1  # Mark as visiting
        for neighbor in graph[course]:
            if visited[neighbor] == 0:  # If neighbor not visited
                if not dfs(neighbor):
                    return False
            elif visited[neighbor] == 1:  # If neighbor is currently being visited, it's cyclic
                return False
        visited[course] = 2  # Mark as visited

numCourses = 2
prerequisites = [[1,0]]
print(canFinish(numCourses, prerequisites)) #true