class Solution:

    def decodeString(self, s: str) -> str:
        if not s:
            return None

        stack = []

        for idx in range(len(s)):
            if s[idx].isdigit() and s[idx+1] == '[':
                rep = s[idx]









