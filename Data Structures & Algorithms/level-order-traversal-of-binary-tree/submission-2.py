from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.traversal = []

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque([])
        queue.append(root)

        while any(queue):

            self.traversal.append([x.val for x in queue])
            
            level_nodes = queue.copy()
            queue = deque([])

            for node in level_nodes:
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)


        return self.traversal


        