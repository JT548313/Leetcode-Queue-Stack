
class Solution:
    def bfs(self, root: str, target: str) -> int:
        if root == target:
            return 0

        queue = [root]
        level = 0

        while len(queue)>0:
            level += 1
            size = len(queue)
            for i in range(size):
                ele = queue.pop()
                if ele == target:
                    return level

                for iterate for next neighbours:
                    queue.append(next neighnours)

        return -1

