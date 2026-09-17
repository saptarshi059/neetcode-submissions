# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _postorder(self, node, path):
        if not node:
            return

        self._postorder(node.left, path)
        self._postorder(node.right, path)
        path.append(node.val)
    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        path = []
        self._postorder(root, path)
        return path