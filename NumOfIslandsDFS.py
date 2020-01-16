from typing import List


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        if not grid:
            return count
        y_max = len(grid)
        x_max = len(grid[0])

        def dfs(x: int, y: int):
            if 0 <= x <x_max and 0 <= y < y_max and grid[y][x] == '1':
                grid[y][x] = '#'
                dfs(x+1,y)
                dfs(x-1,y)
                dfs(x,y+1)
                dfs(x,y-1)

        for y_id in range(y_max):
            for x_id in range(x_max):
                if grid[y_id][x_id] == '1':
                    dfs(x_id, y_id)
                    count += 1

        return count


s = Solution()
