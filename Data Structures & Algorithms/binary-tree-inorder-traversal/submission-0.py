# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        path = []
        if root and root.left:
            path.extend(self.inorderTraversal(root.left))
        if root:
            path.append(root.val)
        if root and root.right:
            path.extend(self.inorderTraversal(root.right))

        return path