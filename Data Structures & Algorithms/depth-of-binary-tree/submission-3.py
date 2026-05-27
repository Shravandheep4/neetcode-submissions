import math

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):

        self.max_height = -1


    def traverse(self, node, height):

        val = node.val if node else None
        print(val ,' ->', height)

        if not node:
            return height - 1

        height = self.traverse(node.left, height + 1)
        height = self.traverse(node.right, height + 1)

        self.max_height = max(self.max_height, height)

        return height - 1
        

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        self.traverse(root, height = 0)

        return self.max_height + 1
        