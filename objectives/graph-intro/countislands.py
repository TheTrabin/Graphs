"""
Understand
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Plan
traverse the grid, whenever you find land, traverse it's connected components and mark them as visited
keep track of number of islands/connected components found
return its count

"""
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        
        numIslands = 0
        width, height = len(grid[0]), len(grid)
        visited = [[False] * width for x in range(height)]
        for y in range(height):
            for x in range(width):
                if grid[y][x] == '1' and not visited[y][x]:
                    numIslands += 1
                    self.iterativeDFT(grid, visited, x, y)
        return numIslands
                    
    def iterativeDFT(self, grid, visited, initialX, initialY):
        width, height = len(grid[0]), len(grid)
        stack = deque()
        stack.append((initialX,initialY))
        while len(stack) > 0:
            x, y = stack.pop()
            if visited[y][x]:
                continue
            visited[y][x] = True
            
            if x - 1 >= 0 and grid[y][x - 1] == '1':
                stack.append((x - 1, y))
            if x + 1 < width and grid[y][x + 1] == '1':
                stack.append((x + 1, y))
            if y - 1 >= 0 and grid[y][x - 1] == '1':
                stack.append((x, y - 1))
            if y + 1 < width and grid[y][x + 1] == '1':
                stack.append((x, y + 1))
    
                