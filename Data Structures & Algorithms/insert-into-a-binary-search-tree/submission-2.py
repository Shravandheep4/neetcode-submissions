# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        node = TreeNode(val)
        head = root
        
        while root:

            # if right node exists then go right, else assign the new node and exit
            if val > root.val:
                if root.right:
                    root = root.right
                else:
                    root.right = node
                    break
                
                

            elif val < root.val :
                if root.left:
                    root = root.left
                else:
                    root.left = node
                    break
        
        else:
            head = node

        return head


             
        