import math


class Solution:
    def numSquares(self, n: int) -> int:
        queue = [(n,0)]
        visited = {(n,0)}
        level = 0

        base = []
        for i in range(math.floor(math.sqrt(n))+1):
            base.append(i**2)

        while queue:
            curr_ele, numOfSums = queue.pop(0)

            if curr_ele in base:
                return numOfSums+1

            for j in reversed(base):
                if curr_ele - j > 0 and curr_ele not in visited:
                    queue.append((curr_ele-j, numOfSums+1))
                    visited.add((curr_ele-j, numOfSums+1))

        return numOfSums


s = Solution()
print(s.numSquares(19))