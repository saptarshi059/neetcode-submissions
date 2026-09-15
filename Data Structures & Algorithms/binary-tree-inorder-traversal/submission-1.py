# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        path = []
        seen = set()
        stack = [root]
        while stack:
            curr = stack[-1]
            left_node = curr.left
            if left_node and left_node.val not in seen:
                stack.append(left_node)
                continue
            
            top = stack.pop()
            path.append(top.val)
            seen.add(top.val)

            if top.right:
                stack.append(top.right)
            

        return path
            