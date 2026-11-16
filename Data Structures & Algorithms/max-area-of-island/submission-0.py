class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0
        currCounter = 0

        def dfs(i: int, j: int):
            nonlocal grid, currCounter

            if i < 0 or j < 0 or i >= ROWS or j >= COLS or grid[i][j] != 1:
                return

            grid[i][j] = 0
            currCounter += 1

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

            return



        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j)
                maxArea = max(currCounter, maxArea)
                currCounter = 0

        return maxArea
            
        