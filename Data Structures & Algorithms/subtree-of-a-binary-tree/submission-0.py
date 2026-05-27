# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def dfs(node, array = []):

            if node is None:
                return array + [None]

            array = dfs(node.left, array)
            array = dfs(node.right, array)

            return array + [node.val]

        tree = dfs(root, [])
        subtree = dfs(subRoot, [])

        
        return subtree in [tree[i:i+len(subtree)] for i in range(len(tree)-len(subtree)+1)]

                



        
        