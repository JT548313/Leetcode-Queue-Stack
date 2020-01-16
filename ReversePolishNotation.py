from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        sign = ['+', '-', '*', '/']
        if not tokens:
            return None

        for t in tokens:
            if t in sign:
                r, l = stack.pop(), stack.pop()
                if t == '+':
                    stack.append(l+r)
                elif t == '-':
                    stack.append(l-r)
                elif t == '*':
                    stack.append(l*r)
                else:
                    if l*r<0 and l%r!=0:
                        stack.append(l//r+1)
                    else:
                        stack.append(l//r)
                continue
            stack.append(int(t))

        return stack.pop()


T = ['4','13','5','/','+']
s = Solution()
print(s.evalRPN(T))