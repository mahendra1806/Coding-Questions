class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def dfs(root,l):
            if root:
                dfs(root.left,l)
                dfs(root.right,l)
                l.append(root.val)
        dfs(root,res)
        return res
        
        
