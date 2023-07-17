# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # count = 0
    # def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
    #     def myps(root, start, tsum):
    #         if not root:
    #             return
    #         tsum -= root.val
    #         if tsum == 0:
    #             self.count += 1
    #         myps(root.left,False,tsum)
    #         myps(root.right,False,tsum)
    #         if start:
    #             myps(root.left,True,tsum)
    #             myps(root.right,True,tsum)
    #     myps(root,True,targetSum)
    #     return self.count
    count = 0
    targetSum = 0
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.targetSum = targetSum
        self.countPath(root,targetSum,True)
        return self.count
    
    def countPath(self,root,curr_sum,isRoot: bool):
        if not root: return 
        curr_sum -= root.val
        if curr_sum == 0:
            self.count += 1
        self.countPath(root.right,curr_sum,False)
        self.countPath(root.left,curr_sum,False)
        
        if isRoot:
            self.countPath(root.right,self.targetSum,True)
            self.countPath(root.left,self.targetSum,True)
