# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.lca = None
        pass


    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        while root:
            value = root.val

            if p.val > value and q.val > value:
                root = root.right
            elif p.val < value and q.val < value:
                root = root.left
            else:
                return root
            







        