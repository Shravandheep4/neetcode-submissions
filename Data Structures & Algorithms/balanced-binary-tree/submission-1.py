# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def traverse(self, node : Optional[TreeNode]) -> int:

        if node is None:
            return 0

        left_depth = self.traverse(node.left)
        right_depth = self.traverse(node.right)

        if abs(left_depth - right_depth) > 1:
            self.balanced = False

        return 1 + max(left_depth, right_depth) 
        

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.balanced = True
        self.traverse(root)

        return self.balanced


        
        