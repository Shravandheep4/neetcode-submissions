# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.order = []

    def traverse(self, node):

        if not node:
            return

        left_subtree = node.left
        right_subtree = node.right

        node.left = right_subtree
        node.right = left_subtree

        self.traverse(node.left)
        self.traverse(node.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        queue = []

        if not root:
            return root

        self.traverse(root)

        return root
        


        