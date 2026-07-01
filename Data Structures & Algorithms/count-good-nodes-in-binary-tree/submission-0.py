# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.maxStack = []
        self.goodnode = 0
    
    def goodNodes(self, root: TreeNode) -> int:

        if root is None:
            return self.goodnode

        if self.maxStack == []:
            self.maxStack.append(root.val)
            
        if self.maxStack[-1] <= root.val:
            self.goodnode +=1
            self.maxStack.append(root.val)

        self.goodNodes(root.left)
        self.goodNodes(root.right)

        if root.val == self.maxStack[-1]:
            self.maxStack.pop()

        return self.goodnode

            



        