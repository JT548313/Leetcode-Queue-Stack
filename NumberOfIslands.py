from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        queue = []
        count = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count += 1
                    queue.append([i, j])
                    grid[i][j] = '0'
                while queue:
                    element = queue.pop()
                    for d in directions:
                        x = element[0] + d[0]
                        y = element[1] + d[1]
                        if 0 <= x < rows and 0 <= y < cols and grid[x][y] != '0':
                            queue.append([x, y])
                            grid[x][y] = '0'

        return count
