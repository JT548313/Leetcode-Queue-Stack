class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if s is None:
            return False

        size = len(s)

        if size % 2 != 0:
            return False

        for i in range(size):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            elif s[i] == ')':
                if stack:
                    s1 = stack.pop()
                    if s1 != '(':
                        return False
            elif s[i] == '}':
                if stack:
                    s1 = stack.pop()
                    if s1 != '{':
                        return False
            elif s[i] == ']':
                if stack:
                    s1 = stack.pop()
                    if s1 != '[':
                        return False

        if len(stack) != 0:
            return False

        return True

s = Solution()
print(s.isValid('(){}[]'))