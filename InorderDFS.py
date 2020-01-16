# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        if not root:
            return None

        stack = [root]
        visited = []
        res = []
        while stack:
            cur_ele = stack[-1]
            if cur_ele not in visited:
                visited.append(cur_ele)
                if cur_ele.left:
                    stack.append(cur_ele.left)
            else:
                result = stack.pop()
                res.append(result.val)
                if cur_ele.right:
                    stack.append(cur_ele.right)

        return res





