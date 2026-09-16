# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _preorder(self, node, path):
        if not node:
            return

        path.append(node.val)
        self._preorder(node.left, path)
        self._preorder(node.right, path)
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        path = []
        self._preorder(root, path)

        return path