import java.util.ArrayList;
import java.util.List;

public class CourseSchedule {

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        } //for
        
        for (int[] prerequisite : prerequisites) {
            graph.get(prerequisite[0]).add(prerequisite[1]);
        }//for

        int[] visited = new int[numCourses];

        for (int i = 0; i < numCourses; i++) {
            if (visited[i] == 0) {
                if (!dfs(i, visited, graph)) {
                    return false;
                } //if
            }//if
        }//for
        return true;
    }//can finish

    private boolean dfs(int course, int[] visited, List<List<Integer>> graph) {
        visited[course] = 1;  // Mark as visiting
        for (int neighbor : graph.get(course)) {
            if (visited[neighbor] == 0) {  // If neighbor not visited
                if (!dfs(neighbor, visited, graph)) {
                    return false;
                } //if
            } else if (visited[neighbor] == 1) {  // If neighbor is currently being visited, it's cyclic
                return false;
            }//elseif
        }
        visited[course] = 2;  // Mark as visited
        return true;
    }//dfs

    public static void main(String[] args) {
        CourseSchedule courseSchedule = new CourseSchedule();
        int numCourses = 2;
        int[][] prerequisites = {{1, 0}};
        System.out.println(courseSchedule.canFinish(numCourses, prerequisites)); //true
    }
}
