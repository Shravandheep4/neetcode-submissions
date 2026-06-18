# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:


        rs_view = []

        queue = []
        queue.append(root)


        while any(queue):

            listnodes = queue.copy()

            rhs = queue.pop()
            rs_view.append(rhs.val)

            queue = []

            for node in listnodes:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return rs_view

        