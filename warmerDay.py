from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        output = [0 for i in range(len(T))]
        stack = list()
        for i in range(len(T)):
            while stack and T[stack[-1]] < T[i]:
                output[stack[-1]] = i - stack[-1]
                stack.pop(-1)
            stack.append(i)

        return output


T = [73, 74, 75, 71, 69, 72, 76, 73]
s = Solution()
s.dailyTemperatures(T)
