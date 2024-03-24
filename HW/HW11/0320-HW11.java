public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
    int originalColor = image[sr][sc];
    if (originalColor != newColor) {
        dfs(image, sr, sc, originalColor, newColor);
    }//if
    return image;
}//floodfill

public void dfs(int[][] image, int row, int col, int color, int newColor) {
    if (row < 0 || row >= image.length || col < 0 || col >= image[0].length || image[row][col] != color) {
        return;
    }//if
    
    image[row][col] = newColor;
    
    dfs(image, row + 1, col, color, newColor);
    dfs(image, row - 1, col, color, newColor);
    dfs(image, row, col + 1, color, newColor);
    dfs(image, row, col - 1, color, newColor);
}//dfs