import sys 
sys.path.append('../functions/')
from tree import TreeNode

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
    	if root == None:
    		return 0
    	else:
    		return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))