def floodFill(self, image, sr, sc, color):    
    if image[sr][sc] != color:
        dfs(image, sr, sc, image[sr][sc], color)
    return image

# Define dfs function separately
def dfs(image, row, col, color, newColor):
    if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]) or image[row][col] != color:
        return
    
    image[row][col] = newColor
    
    dfs(image, row + 1, col, color, newColor)
    dfs(image, row - 1, col, color, newColor)
    dfs(image, row, col + 1, color, newColor)
    dfs(image, row, col - 1, color, newColor)
