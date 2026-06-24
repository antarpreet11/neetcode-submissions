class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        time = 0
        freshOranges = 0
        bfsQ = deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    freshOranges += 1
                elif grid[i][j] == 2:
                    bfsQ.append([i, j])
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while bfsQ and freshOranges > 0:
            for i in range(len(bfsQ)):
                r, c = bfsQ.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if (row < 0 or col < 0 or row == ROWS or col == COLS or grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    bfsQ.append([row, col])
                    freshOranges -= 1
            time += 1
        return time if freshOranges == 0 else -1 



