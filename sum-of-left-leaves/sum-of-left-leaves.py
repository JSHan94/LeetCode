# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = 0
    def sumOfLeftLeaves(self, node: Optional[TreeNode]) -> int:

        def bfs(root,isLeft):
            if root == None :
                return
            if not root.right and not root.left and isLeft :
                self.res += root.val
                
            bfs(root.right, False)
            bfs(root.left, True)
        bfs(node.right, False)
        bfs(node.left,True)
        return self.res