# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            
            if node is None:
                return [True, 0]

            left, right = dfs(node.left), dfs(node.right)

            c1 = left[0]
            c2 = right[0]
            c3 = abs(left[1] - right[1]) <= 1

            balanced = c1 and c2 and c3

            return [balanced, 1 + max(left[1], right[1])]

        balanced, height = dfs(root)

        print(height)

        return balanced