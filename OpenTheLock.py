from typing import List
import queue

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = ['0000']
        visited = {'0000'}
        level = 0

        while len(queue) > 0:
            size = len(queue)
            while size > 0:
                curr_element = queue.pop(0)
                if curr_element == target:
                    return level

                if curr_element in deadends:
                    size -= 1
                    continue

                for i in range(4):
                    s1 = curr_element[:i] + ('9' if (curr_element[i] == '0') else str(int(curr_element[i]) - 1)) + curr_element[i + 1:]
                    s2 = curr_element[:i] + ('0' if (curr_element[i] == '9') else str(int(curr_element[i]) + 1)) + curr_element[i + 1:]

                    if s1 not in visited and s1 not in deadends:
                        queue.append(s1)
                        visited.add(s1)

                    if s2 not in visited and s2 not in deadends:
                        queue.append(s2)
                        visited.add(s2)

                size -= 1
            level += 1

        return -1

deadends = ['8888']
target = '0009'
s = Solution()
print(s.openLock(deadends, target))