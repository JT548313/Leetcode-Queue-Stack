from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:

        if not matrix:
            return

        queue = []
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                count = 0
                cur_ele = matrix[i][j]
                if cur_ele == 0:
                    continue
                else:
                    queue.append((i, j))

        while queue:
            idx, idy = queue.pop(0)
            for (x, y) in direction:
                if 0 <= idx+x < len(matrix) and 0 <= idy+y < len(matrix[0]) and matrix[idx + x][idy + y] == 0:
                    count += 1
                    matrix[idx][idy] = count
                    break
                else:
                    queue.append((idx + x, idy + y))

        return matrix