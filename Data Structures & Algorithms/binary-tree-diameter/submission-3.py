# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.max_diameter = 0

    def find_depth(self, node, height, max_height):

        if not node:
            return (height - 1), max_height

        height, max_height = self.find_depth(node.left, height + 1, max_height)
        height, max_height = self.find_depth(node.right, height + 1, max_height)

        max_height = max(height, max_height)

        return (height - 1), max_height

    def traverse(self, node):
        
        if node is None:
            return
        
        current_node = node

        # Find the max height of the left and right sub tree
        _, l_height = self.find_depth(current_node.left, 1, 0)
        _, r_height = self.find_depth(current_node.right, 1, 0)

        height = l_height + r_height

        self.max_diameter = max(height, self.max_diameter)

        self.traverse(node.left)
        self.traverse(node.right)

        return

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.traverse(root)

        return self.max_diameter
    

        
        