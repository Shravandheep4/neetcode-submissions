# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self):
        self.max_depth = 0

    def traverse(self, node: Optional[TreeNode], depth : int) -> int:

        if node is None:
            return depth - 1
        
        self.max_depth = max(depth, self.max_depth)
        
        depth = self.traverse(node.left, depth + 1)
        depth = self.traverse(node.right, depth + 1)

        return depth - 1

    def maxDepth(self, root: Optional[TreeNode], depth=0) -> int:

        self.traverse(root, 1)
        return self.max_depth
