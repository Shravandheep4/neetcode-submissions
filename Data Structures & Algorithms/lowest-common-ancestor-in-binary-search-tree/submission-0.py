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

        value = root.val

        if p.val > value and q.val > value:
            self.lowestCommonAncestor(root.right, p, q)
        elif p.val < value and q.val < value:
            self.lowestCommonAncestor(root.left, p, q)
        else:
            self.lca = root

        return self.lca
            







        