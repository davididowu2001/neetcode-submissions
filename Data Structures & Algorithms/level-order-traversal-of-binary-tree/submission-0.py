# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []
        def dfs(node, level):
            if not node:
                return None
            
            if len(res) == level:
                res.append([])
            res[level].append(node.val)
            dfs(node.left, level+1)
            dfs(node.right, level+ 1)
        dfs(root, 0)
        return res
'''
Algorithm

res = []
dfs(node, level):

the idea is you use the length of the result to keep track of the levels. e.g
len(res) = 0 meaning u are in level 0
so append "[]" at level 0 to res, then add 0 to the res[level].
now, res is len of 1 cuz [1] in list
so for level 1, you check that length of res matches level, indicating same level
add the left node, res = [[1], [2]]
base case again: and turns out len (res) is 2 and matches the lvel
so add right node, res = [[1], [2,3]]
'''