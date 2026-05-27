# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        
        def inorder(node, order = []):

            if node is None:
                return order + [None]
            
            order = inorder(node.left, order)
            order = inorder(node.right, order)

            return order + [node.val]

        left_list = inorder(p, order = [])
        right_list = inorder(q, order = [])

        return left_list == right_list


        