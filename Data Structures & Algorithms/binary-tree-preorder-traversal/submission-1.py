# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        path = []
        stack = [root]
        seen = set()
        
        while stack:
            top = stack[-1]
            if top.val not in seen:
                path.append(top.val)
                seen.add(top.val)

            if top.left and top.left.val not in seen:
                stack.append(top.left)
                continue
            
            if top.right and top.right.val not in seen:
                stack.append(top.right)
                continue
            
            stack.pop()
        
        return path 